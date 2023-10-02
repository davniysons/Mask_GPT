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

    def format_prompt(self, text):
        placeholders = {
            "[NAME]": "[NAME]",
            "[ADDRESS]": "[ADDRESS]",
            "[PHONE]": "[PHONE]"
        }
        
        # Construct the prompt
        formatted_prompt = prompt.format(text=text)
        return formatted_prompt

    def call_gpt_api(self, formatted_prompt):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=formatted_prompt,
            max_tokens=500,
            api_key=openai.api_key,
            temperature=0.2
        )
        return response

    def extract_masked_data(self, masked_text):
        sections = masked_text.split('%%%')
        masked_data = sections[1]

        pattern = r"\[([A-Z]+)\]: '([^']+)'"
        matches = re.findall(pattern, masked_data)

        masked_data_dict = {key: value for key, value in matches}
        return masked_data_dict

    def mask_personal_data_with_gpt(self, text):
        # Format the prompt
        formatted_prompt = self.format_prompt(text)

        # Call the GPT-3.5 API to get the masked text
        response = self.call_gpt_api(formatted_prompt)
        
        # Replace the placeholders in the response with the appropriate masked data
        masked_text = response["choices"][0]["text"]
        placeholders = {
            "[NAME]": "[NAME]",
            "[ADDRESS]": "[ADDRESS]",
            "[PHONE]": "[PHONE]"
        }
        for key, value in placeholders.items():
            masked_text = masked_text.replace(key.upper(), value)

        # Extract and return the masked data dictionary
        masked_data_dict = self.extract_masked_data(masked_text)

        text_checked = text
        for key, value in masked_data_dict.items():
            text_checked = text_checked.replace(f"[{key}]", value)

        if text == text_checked:
            return masked_text.split('%%%')[0]
        else:
            return False
        
        