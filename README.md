# checkmarx-tech-assessment - cloc-app
## Use cloc to generate a report which is then sent via email to a specified address as a .csv

* * *

Cloc-app uses python to pull a desired git repository and then use CLOC (Count Lines of Code, a project by Al Danial, who's Github can be found here https://github.com/AlDanial) to generate a report based off of a scan of the repo. The scan generates a report in .csv format which is then emailed to an email of your choosing.

* * *

### Required installations
- Python 3.10.4
    - You'll need pip in order to install gitPython
        - This can be installed by using ```"pip install gitpython"``` in the CLI of your choosing
- Git
- Gmail account which will be used to send the report
    -Must have email account and password, for authentication
    -**IMPORTANT** You must have *Less secure app access* enabled in your google account settings or else Google will block account access! This setting will go away May 30th, 2022, so this app will no longer function past that date. (Unless I update it and utilize a different method of sending the email)
    -The receiving email does not have to be a gmail account


### Basic Use
Run the cloc-app.py file and input the values that you are prompted for! The .csv file that will be sent will include the following information.
- **files** : How many files, broken down by language
- **language** : The individual languages used in the project
- **blank** : How many lines are blank in each languages corresponding file types
- **comment** : How many lines are comments in each languages corresponding file types
- **code** : How many lines are code in each languages corresponding file types