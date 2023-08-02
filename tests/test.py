import unittest
from Mask.mask import Mask

class MyTest(unittest.TestCase):
    def setUp(self):
        self.mask = Mask()

    def test_mask_name(self):
        self.assertEqual(self.mask.mask_name(
            """I had an amazing time at The Riverside Cafe with my friend Sarah Johnson. The address, 123 Main Street, Pleasantville, was easy to find. The food was delightful, 
            and the service was top-notch. Don't forget to try their special desserts! You can reach them at +1 (555) 123-4567. Highly recommended!"""), True)

if __name__ == '__main__':
    unittest.main()


