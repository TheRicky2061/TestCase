#!/usr/bin/env python
'''
Create a new directory for some project. 
Prints the ID of the newly created directory in JSON Format:

{"folder_link" : "<path to projects folder>/<user_id>/<project_identifier>"}
'''

__filename__  = "new_dir.py"
__author__    = "Enrique Rodriguez"
__email__     = "enrique.rodriguez9@upr.edu"
__version__   = "1.0.4"
__credits__   = ["Bryan Pesquera", "David Ortiz", "Enrique Rodriguez", "Kevin Legarreta", "Luis Mieses"]
__copyright__ = "Copyright 2018, Grafia"


from uuid import uuid4                                      # Used for naming project directories with random identifiers.
import os                                                   # Used for creating the directory.
import json                                                 # Used for outputing the directory name.
import sys                                                  # argv, exit

PATH = "projects/"                                          # Location where the directories will be stored.

def main():
    ''' Main Program. '''
    user_id = sys.argv[1]
    
    if user_has_no_folder(PATH, user_id):                       # Check if the user directory exists.
        create_user_directory(PATH, user_id)                    # if not, create it.
    
    json = create_project_directory(PATH, user_id)

    print(json)

def create_user_directory(path, user):
    ''' Creates a user directory at the given path. Returns True if the user was created.  '''
    if type(user) is not str:
        raise TypeError("Expected type 'str' got '{}'".format(user.__class__.__name__))

    user_path = os.path.join(path, user)
    try:
        os.mkdir(user_path)                                 
    except:
        return False
    return True

def user_has_no_folder(path, user = ''):
    ''' Returns true if the user does not have a projects folder of his/her own. '''
    user_path = os.path.join(path, user)
    return not os.path.exists(user_path)

def is_number(num_string):
    ''' Returns true if parameter is a number, false otherwise'''
    try:
        int(num_string)
    except ValueError:
        return False
    return True

def create_subfolders(path):
    '''
    Create the default project folders for a given project path.
    Images, Videos, Documents, Voice Recording.
    '''

    sub_folders = ["images", "docs", "videos", "voice"]

    for folder_name in sub_folders:
        sub_folder_path = os.path.join(path, folder_name)   # i.e. "/path/to/project/images/"
        os.mkdir(sub_folder_path)
    
def create_project_directory(path, user=''):
    '''
    Creates a project directory at the given path.
    Returns a JSON string of the absolute path of the newly created project directory.
    '''
    if type(user) is not str:
        raise TypeError("Expected type 'str' got: '{}'".format(user.__class__.__name__))
    
    user_path = os.path.join(path, user)

    if not os.path.exists(user_path):
        raise ValueError("Invalid Path: {}".format(user_path))                   # Verify that the given path exists.

    directory_name = str(uuid4())                           # The name that will be assigned to the project's directory name.
    no_file_created = True

    while no_file_created:

        folder_link = os.path.join(user_path, directory_name)

        try:
            os.mkdir(folder_link)                           # Create the new directory at user path.
            no_file_created = False
        except:
            directory_name = str(uuid4())                   # Generate a different name if it already exists (Unlikely, but just in case).
    
    create_subfolders(folder_link)                          # Create necessary project subfolders for that project.
    directory_path = {"folder_link" : folder_link} 

    return json.dumps(directory_path)                       # i.e. {"folder_link" : "/var/www/projects/2/8dafab93-1342-404b-87c1-104f26e9a14b"}

if __name__ == "__main__" : 
    if len(sys.argv) != 2: 
        sys.exit("Not enough arguments. Exiting...")
    
    if not is_number(sys.argv[1]): 
        sys.exit("Argument must be a number. Exiting...")

    main()
