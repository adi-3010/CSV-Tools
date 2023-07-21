
This repository contains scripts that allow the conversion of html tables to CSV files and to insert CSV data into an appropriate pre-existing SQLite3 Table. Directions to use the scripts are given below:

## To Convert HTML Table to CSV:

1) Put the code of the html table in the input.txt file. To make sure that the code runs properly, only include the tbody. The code **DOES NOT** recognise table headings and will ignore them.
2) Run the HTML-CSV.py script. You should get an output.csv file with | as the delimiter for your data. If you are fine with that delimiter, you can use your csv file as such. Or else, you can go to step 3
3) Run the delimiterconvert.py script. Now you should get a file called output_final.csv which is delimited by commas. Note that all fields will be enclosed by quotes.<br><br>
**NOTE:** The code to convert the table ignores a particular combination of spaces before and after the data. This will be fixed in future versions to ignore all spaces before and after the data

## To insert data from CSV files into an SQLite3 Table:

1) To use this script you will need to create an SQLite3 database with a table with the appropriate number of fields with the correct field data types. If you have already created such a table in a database and wish to use the same, ignore this step.
2) Once you have created the database, paste it into the same folder as CSV-SQL.py. 
3) Rename the CSV file from which the data is to be inserted to input.csv and put it in the same folder as the script and the database.
4) Enter the name of the database with the correct extension. Next, enter the name of the table which will hold the data. This is the same table that is mentioned in step 1.
5) After entering the table name, all the data will be inserted into the table and committed.<br><br>
**NOTE:** In future versions, you will be able to check the changes made to the table before deciding whether to commit or not.