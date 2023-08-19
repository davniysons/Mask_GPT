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

class MyTest(unittest.TestCase):
    def test_mask_name(self):
        mask = Mask()

        if type(test_text) == str:
            result = mask.mask_personal_data_with_gpt(test_text)
            print(result)
        
        else:
            for i, unmasked_text in enumerate(test_text['unmasked']):
                text = unmasked_text
                result = mask.mask_personal_data_with_gpt(text)
                print(result)
                time.sleep(20)

        

if __name__ == '__main__':
    unittest.main()


