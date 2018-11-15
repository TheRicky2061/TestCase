from new_dir.new_dir import is_number
import unittest

class TestIsNumber(unittest.TestCase):
    
    def test_digit_str(self):
        number = is_number('1')
        self.assertTrue(number)
    
    def test_word(self):
        number = is_number('number')
        self.assertFalse(number)
    
    def test_float(self):
        number = is_number('3.4')
        self.assertFalse(number)
    
    def test_number_str(self):
        number = is_number('88')
        self.assertTrue(number)

if __name__ == "__main__" : 
    unittest.main()

