import csv, sqlite3, os
#Function to get data from input.csv and convert it into a list
def get_list():
    List = []
    with open(os.path.dirname(__file__)+"\\input.csv",'rt') as f:
        reader = csv.reader(f)
        for row in reader:
            List.append(tuple(row))
    return List

#Function to insert data into table
def parse(data):
    for line in data:
        crsr.execute("INSERT INTO {} VALUES {};".format(table_name,str(line)))

db_name = input("Enter the database name: ")+'.db'
cnct = sqlite3.connect(db_name)
crsr = cnct.cursor()
table_name = input("Enter the name of the table: ")
parse(get_list())
cnct.commit()