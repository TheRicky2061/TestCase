from new_dir.new_dir import user_has_no_folder
import unittest
import os
    
CWD = os.getcwd()
USERS_DIRECTORY = os.path.join(CWD, "test/users")

class TestUserHasNoFolder(unittest.TestCase):

    def test_invalid_user(self):
        user = '1'
        no_folder = user_has_no_folder(USERS_DIRECTORY, user)
        self.assertTrue(no_folder)
    
    def test_valid_user(self):
        user = '2'
        no_folder = user_has_no_folder(USERS_DIRECTORY, user)
        self.assertFalse(no_folder)
    
    def test_invalid_path_type(self):
        user = '2'
        directory = True

        with self.assertRaises(TypeError):
            no_folder = user_has_no_folder(directory, user)
    
    def test_invalid_user_type(self):
        user = 3.14
        
        with self.assertRaises(TypeError):
            no_folder = user_has_no_folder(USERS_DIRECTORY, user)


if __name__ == "__main__" : 
    unittest.main()

