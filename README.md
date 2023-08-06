# Python API Automation Framework

###  Integration Test cases for the Restful Booker
URL - https://restful-booker.herokuapp.com/apidoc/index.html

1. Verify GET, POST, PATCH, DELETE, PUT
2. Response Body, Headers, Status Code.
3. Auth - Basic Auth, Cookie Based Auth.
4. JSON Schema Validation.


###  Tech Stack (Python Packages used)
1. Python, Request Module
2. PyTest, PyTest-html
3. Allure Report
4. Faker, CSV, JSON, YAML.
5. Run via Commandline - Jenkins

#### P.S - DB Connection(in future)

## Install pip package
- `pip install requests pytest pytest-html faker allure-pytest jsonschema`
- `pip install requirements.txt`
- `pip install python-dotenv`
- `pip install pytest-xdist`
- `pip install allure-pytest`

# How to work with Allure Report?
--> Install the dependencies in requirements.txt file: 
- allure-pytest==2.13.2

--> Install Node.js from Google Site
--> Verify its installation by running the following commands in CMD:-
- node --version
- npm --version

--> If the user is able to see above version number in CMD:

# Run the below commands in CMD terminal to assure allure installation
- allure commandline npm
- npm i -g allure-commandline
- allure (To verify it's properly installed)
- Add Allure to system path by Editing the system environment variables (C:\Users\Sukhmani\AppData\Roaming\npm\node_modules\allure-commandline\bin)

# [Optional] Run Powershell in administrator mode and run below commands to check the allure status?
- Enter allure and hit enter
- if nothing happens, then run Get-ExecutionPolicy---> If Output is Restricted, means Powershell scripts are disabled on machine 
- To Enable it, run Set-ExecutionPolicy RemoteSigned--->Y
- To Revert back, run Set-ExecutionPolicy Restricted--->Y 

**Note:-** Mark the TC's with below Annotations:
- import pytest, allure
- @pytest.mark.smoke
- @allure.feature("TC#1 - Verify <Feature Name>")

## How to run Locally and see the HTMl and Allure Report?
- `pytest --alluredir=./reports (It will create reports folder only under Project`
- `pytest tests/* -s -v --alluredir=./reports --html=report.html`
              *************OR**************
- `pytest .\tests\intergration_tests\test_create_booking.py -s -v --html=report.html --alluredir=./reports`

**_Note_**: After reports folder is created successfully under Project containing JSON files, now in order to see allure report, run the below command: 
--> Right Click ---> Project--->Open In Explorer--->Click the Project--->type cmd in the path of the project and run below command in **system cmd** to generate allure report
- `allure serve ./reports` (Run only in System CMD)


## How to Run via Jenkins?
-->Build Steps:
cd C:\Users\Sukhmani\.jenkins\workspace\RunPythonAPIAutomationTestScriptsFromGitHub
# python --version
# Install
pip install -r requirements.txt
pytest .\tests\intergration_tests\test_create_booking.py -s -v --html=report.html --alluredir=./reports
