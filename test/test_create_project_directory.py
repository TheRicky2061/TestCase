from new_dir.new_dir import create_project_directory
import os
import unittest

PATH = "test/projects"
CWD = os.getcwd()
PROJECTS_PATH = os.path.join(CWD, PATH)
    
class TestCreateProjectDirectory(unittest.TestCase):
     
    def test_valid_path(self):
        ''' Create Project Directory at a Valid Path. '''
        try:
            create_project_directory(PROJECTS_PATH)
        except Exception as e:
            self.fail("An exception was raised: {}".format(e))

    def test_invalid_path(self):
        ''' Verify that an exception is raised if path is invalid. '''
        invalid_path = "Hello, Word"
        with self.assertRaises(ValueError):
            create_project_directory(invalid_path)

    def test_invalid_type(self):
        ''' Confirm that a TypeError is raised if the type given is not 'str'. '''
        with self.assertRaises(TypeError):
            create_project_directory(1)

if __name__ == "__main__" : 
    unittest.main()

