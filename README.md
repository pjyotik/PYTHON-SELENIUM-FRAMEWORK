# Python Selenium Web Framework 


Setup the Framework in Local :

1. Create a Virtual Environment (Win):
     
     $ virtualenv --python C:\Users\prano\AppData\Local\Programs\Python\Python38\python.exe venv
     
     $ .\venv\Scripts\activate
    
     $ deactivate       [Command to deactivate the Virtual environment]
     

2. Install packages into virtual env and Run below command:
   
   - $ pip freeze > requirements.txt  [ requirement.txt has all the relevant packages installed ]
   
3. Rules to Write Test cases.
 
    - FileName should start or end with test 
        [example : test_login or login_test]
    
    - Class name and methods names should also follow the same naming convention, camelcase in case of Class Name 
        [example: def test_sample1() ] and [example: class BaseTest]


5. Command to Run:
    
    $ pytest src/tests/NopCommerce/test_login.py -s -v -n=2 --html=reports/AutomationReport.html --browser=chrome
    
    pytest src/tests/SwagLabs -sv -n=2 --html=test-output/reports/AutomationReport.html --browser=chrome
    
    $ pytest Tests/nopcommerce/<TEST-CASE-NAME> -sv -m "sanity" --html=reports/AutomationReport.html --browser=chrome
    
    [arguments]
    -s          -> To display the print Statements in console
    -v          -> For more verbose or information
    -n          -> This is for running parallel with no of threads
    -m          -> markers
    --html      -> To generate html reports
    --browser   -> select the browser
 
    
    
    
 
    