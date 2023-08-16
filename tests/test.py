import unittest
import os
import sys
import json
import time

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, parent_dir)


from Mask.mask import Mask

with open('test_data/test_examples_2.json', 'r') as file:
    json_data = file.read()
test_text = json.loads(json_data)



# class MyTest(unittest.TestCase):

#     def test_mask_name(self):
#         mask = Mask()
#         text = test_text['unmasked'][5]

#         result = mask.mask_personal_data_with_gpt(text)
        
#         print('\nBEFORE:')
#         print(text)
#         print('\nAFTER:')
#         print(result)
    

class MyTest(unittest.TestCase):
    def test_mask_name(self):
        mask = Mask()
        correct_count = 0  

        for i, unmasked_text in enumerate(test_text['unmasked']):
            text = unmasked_text
            result = mask.mask_personal_data_with_gpt(text)
            result = result[0].lstrip('. \n')

            print('\nBEFORE:')
            print(text)
            print('\nAFTER:')
            print(f"'{result}'")

            if result == test_text['masked'][i]:
                print('Correct')
                correct_count += 1
            else:
                print('Incorrect masking')

            if i < len(test_text['unmasked']) - 1:
                time.sleep(20)
        
        percentage_correct = (correct_count / len(test_text['unmasked'])) * 100
        print('\nCorrect masked %:')
        print(percentage_correct)

if __name__ == '__main__':
    unittest.main()


