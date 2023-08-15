import unittest
import os
import sys
import json
import time

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, parent_dir)


from Mask.mask import Mask

with open('test_data/test_examples.json', 'r') as file:
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
        for i in range(len(test_text['unmasked'])):
            mask = Mask()
            text = test_text['unmasked'][i]

            result = mask.mask_personal_data_with_gpt(text)
            result = result[0]
            result = result.lstrip('. \n')

            print('\nBEFORE:')
            print(text)
            print('\nAFTER:')
            print(f"'{result}'")

            correct = 0
            if result == test_text['masked'][i]:
                print('Correct')
                correct += 1
            else:
                print('Incorrect masking')

            time.sleep(20)
            print('Correct masked %:')
            print(correct / len(test_text['unmasked']) * 100 )

if __name__ == '__main__':
    unittest.main()


