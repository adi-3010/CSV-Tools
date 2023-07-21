import os, csv
#Store the csv file's data as a nested list using csv(This effectively converts the data into comma delimited values)
List =[]
with open(os.path.dirname(__file__)+"\\output.csv",'rt') as data:
    read = csv.reader(data, delimiter='|')
#Remove the comment from the next line if your first line has a header that you don't want to include
#    next(read)
    for row in read:
        List.append(row)
with open(os.path.dirname(__file__)+"\\output_final.csv",'wt') as f:
    write = csv.writer(f, skipinitialspace=True, lineterminator="\n", quoting=csv.QUOTE_NONNUMERIC)
    write.writerows(List)