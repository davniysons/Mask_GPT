import openai
import pandas as pd
import os

api_key = os.getenv("OPENAI_API_KEY")
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
            Please keep the original text unchanged and do not add any additional content or modify the provided text.'''


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

        if mask_text != masked_text:
            return masked_text
        else:
            return False

