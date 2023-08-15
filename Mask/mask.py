import openai
import pandas as pd
import os
import re

# api_key = os.getenv("OPENAI_API_KEY")
api_key = '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'
openai.api_key = api_key

class Mask:
    def __init__(self):
        pass

    def mask_personal_data_with_gpt(self, text):
        mask_text = text
        placeholders = {
            "[NAME]": "[NAME]",
            "[ADDRESS]": "[ADDRESS]",
            "[PHONE]": "[PHONE]"}
    
        # Create a template for the prompt, indicating the personal data types to mask
        prompt = f'''Please mask any personal information, such as name, surname or full name (including variations of first and last names and anything you consider a name),
            address (including variations of street names, city names, index, region and country), and phone (including variations of phone numbers)
            using the following tokens: [NAME], [ADDRESS], [PHONE] in the following text:

            {text}

            Always consider that you are seeing this text for the first time.
            If the address consists of multiple words and punctuation marks, combine them into a single mask.
            Please keep the original text unchanged and do not add any additional content or modify the provided text.
            After that - add '%%%' in the end of returned text,
            and add at the end dictionary such as [NAME]: 'name what masked', [ADDRESS]: 'address what masked', etc'''


        # Call the GPT-3.5 API to get the masked text
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=500,
            api_key=api_key,
            temperature = 0.2
        )
        
        # Replace the placeholders in the response with the appropriate masked data
        masked_text = response["choices"][0]["text"]
        for key, value in placeholders.items():
            masked_text = masked_text.replace(key.upper(), value)

        sections = masked_text.split('%%%')
        masked_text = sections[0]
        masked_data = sections[1]

        pattern = r"\[([A-Z]+)\]: '([^']+)'"
        matches = re.findall(pattern, masked_data)

        masked_data_dict = {key: value for key, value in matches}

        if mask_text != masked_text:
            return masked_text, masked_data_dict
        else:
            return False, masked_data_dict
        
        
####################################    
## FUNCTION TO CHECK PLACEHOLDERS ##
####################################

    def has_placeholders(self, text):
        placeholders = ["[NAME]", "[ADDRESS]", "[PHONE]"]
        for placeholder in placeholders:
            if placeholder in text:
                return True
        return False
    
####################################    
## FUNCTION TO CHECK VALID CHANGE ##
####################################




# mask_instance = Mask()
# text = '''I had an amazing time at The Riverside Cafe with my friend Sarah Johnson. The address, 123 Main Street, Pleasantville, was easy to find. The food was delightful, and the service was top-notch. Don't forget to try their special desserts! You can reach them at +1 (555) 123-4567. Highly recommended!'''

# #text = 'Julie Smith lives at 123 Firth Street, San Francisco. Her phone number is 555-1234.'

# result, masked_data = mask_instance.mask_personal_data_with_gpt(text)

# if mask_instance.has_placeholders(result):
#     print('\nBEFORE:')
#     print(text)
#     print('\n\nAFTER:')
#     print(result)
#     print(masked_data)
# else:
#     print('NOTHING TO CHANGE')
#     print(text)  
#     print(identified_data)

# ######################################
