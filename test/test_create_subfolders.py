from new_dir.new_dir import create_subfolders
import os
import unittest

PATH = "test/subfolders"
CWD = os.getcwd()
SUBFOLDERS_PATH = os.path.join(CWD, PATH)
    
class TestCreateSubfolders(unittest.TestCase):
    
    def test_subfolder_creation(self):
        ''' Creates the subfolders at the path. '''
        try:
            create_subfolders(SUBFOLDERS_PATH)
        except:
            print("Folders Exists. Please delete subfolders to run test.") 

    def test_verify_subfolder_creation(self):
        ''' Verifies that the subfolders were in fact created. '''

        for subfolder in ['images', 'docs', 'voice', 'videos']:    
            if subfolder not in os.listdir(SUBFOLDERS_PATH):
                self.fail()
        
if __name__ == "__main__" : 
    unittest.main()

