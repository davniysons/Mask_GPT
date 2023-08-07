import unittest
import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, parent_dir)


from Mask.mask import Mask

class MyTest(unittest.TestCase):

    def test_mask_name(self):
        mask = Mask()
        text = """I had an amazing time at The Riverside Cafe with my friend Sarah Johnson. The address, 123 Main Street, Pleasantville, was easy to find. The food was delightful, 
            and the service was top-notch. Don't forget to try their special desserts! You can reach them at +1 (555) 123-4567. Highly recommended!"""

        result = mask.mask_personal_data_with_gpt(text)
        
        print('\nBEFORE:')
        print(text)
        print('\n\nAFTER:')
        print(result)


if __name__ == '__main__':
    unittest.main()


