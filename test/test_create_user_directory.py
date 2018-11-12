from new_dir.new_dir import create_user_directory
import os
import unittest
import random

PATH = "test/users"
CWD = os.getcwd()
ALL_USERS_PATH = os.path.join(CWD, PATH)

class TestCreateUserDirectory(unittest.TestCase):
    
    def test_create_valid_user(self):
        ''' Creates a new user directory at given path. '''
        user = str(random.randint(1,1000000000))
        created = create_user_directory(PATH, user)
        
        self.assertTrue(created)

    def test_invalid_user(self):
        ''' Verify that an exception is raised if an invalid user is given. '''
        user = 123
        with self.assertRaises(TypeError):
            created = create_user_directory(PATH, user)

if __name__ == "__main__" : 
    unittest.main()

