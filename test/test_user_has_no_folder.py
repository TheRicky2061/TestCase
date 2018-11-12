from new_dir.new_dir import user_has_no_folder
import unittest
import os
    
CWD = os.getcwd()
PROJECTS_FOLDER = os.path.join(CWD, "test/users")

class TestUserHasNoFolder(unittest.TestCase):

    def test_1(self):
        user = '1'
        no_folder = user_has_no_folder(PROJECTS_FOLDER, user)
        self.assertTrue(no_folder)
    
    def test_2(self):
        user = '2'
        no_folder = user_has_no_folder(PROJECTS_FOLDER, user)
        self.assertFalse(no_folder)
    

if __name__ == "__main__" : 
    unittest.main()

