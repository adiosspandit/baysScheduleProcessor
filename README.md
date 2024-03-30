README

* update the Roster template in roster_templates/ directory with your club name
Default template containes Town/Club: Northborough Youth Soccer Association

* Review the python script top section to match the column names in your team snap export
* Team names must be in a column named Team
* Other fields like first , last etc. can be adjusted but 
it is suggested to just match the column names as expected in the script as 
you will just need to adjust the header row of your export
LAST='last'
FIRST='first'
GRADE='Grade Level'
BIRTH='birthdate'
CITY='city'
GENDER='gender'

Pre-requisites: Python 3.8 or above 
Make sure you install or have following modules
pip3 install python-docx
pip3 install pandas

Run:
python3 ./ts2baysroster.py --teamExcelFile /Users/adi/Downloads/myTeamSnapExport.xlsx

Known Issues:
* For mixed grade teams the program just picks the last players grade and puts it as the Teams grade level
* It does not add Coaches names. Those will need to be added manually.
