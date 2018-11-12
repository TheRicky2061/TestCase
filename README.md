# User Story Test Case

Test case for one of my user stories. The user story that i've chosen for this assigment says the following:
```
Como usuario deseo que la creación de mi proyecto reserve un espacio en el servidor para mis datos. 
Tiempo estimado: 1.5 días
Definición de completado: Cada proyecto tiene su propia región de almacenar data.
Notas de implementación: Debe ser desde la misma aplicación.
```
When creating a new project and inserting it into the database, a set of directories and subdirectories must be created. If the user that is creating a new project does not have a projects directory, it must be created. Furthermore, the project directory must also be created. Inside each project directory must exist the following subdirectories: images, documents, videos and voice memos.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

To Run these test cases, your local machine must have the following:

* python version 2 or 3 installed.
* unittest module (installed by default)

### Installing

No additional dependencies are required to run these unittest test cases. This python program is self contained and only uses libraries provided by python's pre-installed packages.

## List of test cases.

* test_create_project_directory.py
* test_create_user_directory.py
* test_is_number.py
* test_user_has_no_folder.py
* test_create_subfolders.py

## Running the tests

To run a test, first make sure that you are inside the "testing" directory(The same directory this readme is in). To run a specific test, run the following command from the terminal.
```
python -m unittest test.test_to_run
```
For Example:
```
python -m unittest test.test_create_project_directory
```
If all tests pass, a similar message to the one below will appear:
```
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```
Each "dot"(.) before the separator represents a test case, if one of the test cases does not succeed, it will be replaced with an "F" if there's a failure or an "E" if there was an error running the test.

If you want to run every test case cuncurrently, type the following into the terminal:
```
python -m unittest discover
```
As mentioned, this command must be runned from the "testing" directory.
The output should look similar to the following:
```
.............
----------------------------------------------------------------------
Ran 13 tests in 0.002s

OK
```

## Authors

* Enrique Rodriguez 

