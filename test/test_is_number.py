from new_dir import new_dir
import unittest

class TestIsNumber(unittest.TestCase):
    
    def test_1(self):
        number = new_dir.is_number('1')
        self.assertTrue(number)
    
    def test_2(self):
        number = new_dir.is_number('number')
        self.assertFalse(number)
    
    def test_3(self):
        number = new_dir.is_number('3.4')
        self.assertFalse(number)
    
    def test_4(self):
        number = new_dir.is_number('88')
        self.assertTrue(number)

if __name__ == "__main__" : 
    unittest.main()

