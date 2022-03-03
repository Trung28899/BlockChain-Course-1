## TESTING THE APPLICATION: TABLE OF CONTENT:

1, 8th Commit: Python file setup & Virtual environment
2, 9th Commit: Test the application (Basic of how to run test in python)
3, 10th Commit: Added more tests

---

## FUNDAMENTALS:

1, Files structure in python (8th Commit):

- `__init__.py` files :
  +, Informing that we're treating this directory as a python package

- Here is how to execute a python file:
  +, $ cd "Test the Application"
  +, $ python3 -m backend.blockchain.block
  +, if this doesn't work, you might want to create a file named: `__init__.py` files
  and try again to see if it works

---

## COMMANDS:

1, How to create and enter virtual environments (8th Commit):

`$ python3 -m venv blockchain-env`
=> Create a virtual environment

`$ source blockchain-env/bin/activate`
=> Enter the virtual environment

`$ echo $VIRTUAL_ENV`
=> Get the virtual environment directory

In virtual environment, we can install the packages and it won't affect
other packages

2, Install packages (8th Commit):

`$ pip3 install pytest==5.1.2`

pip3 is a package manager (like npm)
pytest==5.1.2: pytest is the package, 5.1.2 is the version of the package

See file requirements.txt

any developer can run this command and all the packages will be installed:

`$ pip3 install -r requirements.txt`

---

## COMMIT HISTORY:

1, 8th Commit: Python file setup & Virtual environment

2, 9th Commit: Test the application

**Run the tests**

    - Any file with prefix of test will be executed when you run the command

    - Make sure to activate the virtual environment

`$ python3 -m pytest backend/tests`

    - See file: ./"Test the Application"/backend/tests

3, 10th Commit: Added more tests

    - See folder: ./"Test the Application"/backend/tests

Run: `$ python3 -m pytest backend/tests`
