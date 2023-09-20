import openai
import pandas as pd
import os
import re

openai.api_key = os.getenv("OPENAI_API_KEY")

# Define the prompt outside of the class
prompt = '''
Please mask any personal information, such as name, surname or full name (including variations of first and last names and anything you consider a name),
address (including variations of street names, city names, index, region and country), and phone (including variations of phone numbers)
using the following tokens: [NAME], [ADDRESS], [PHONE] in the following text:
{text}
Always consider that you are seeing this text for the first time.
If the address consists of multiple words and punctuation marks, combine them into a single mask.
Please keep the original text unchanged and do not add any additional content or modify the provided text.
After that - add '%%%' in the end of returned text,
and add at the end dictionary such as [NAME]: 'name what masked', [ADDRESS]: 'address what masked', etc
'''

class Mask:
    def __init__(self):
        pass

    def mask_personal_data_with_gpt(self, text):
        placeholders = {
            "[NAME]": "[NAME]",
            "[ADDRESS]": "[ADDRESS]",
            "[PHONE]": "[PHONE]"}
    
        # Inject the input text into the prompt
        formatted_prompt = prompt.format(text=text)

        # Call the GPT-3.5 API to get the masked text
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=formatted_prompt,
            max_tokens=500,
            api_key=openai.api_key,
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

        text_checked = text
        for key, value in masked_data_dict.items():
            text_checked = text.replace(f"[{key}]", value)

        if text == text_checked:
            return masked_text
        else:
            return False
