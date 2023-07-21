import os
# Function to get data from input.txt
def get_input():
    with open(os.path.dirname(__file__)+'\\input.txt','rt') as fi:
        input_data = fi.read()
        return input_data
#Function to convert data containing html table to csv data delimited by |(can be replaced with another script later)
def parse(data):
    output=""
    # Checks for the < character. If found scans the next two or three characters. If td is found, takes whatever is between the next > and < and adds it to the output string followed by the delimiter(slightly scuffed code has been added to remove spaces from the beginning and end of the data).
    # If \tr is found, a newline character is added to the output string
    for i in range(len(data)):
        if data[i]== "<":
            if data[i+1:i+3]=="td":
                for j in range(i,len(data)):
                    if data[j]==">":
                        for x in range(j,len(data)):
                            if data[x] == "<":
    #                            output+=data[j+1:x]+'|'
    # These if statements can be replaced by a function that checks if the first characters of the data string are spaces and removes them and does the same for the reverse(logic is better explained in the docs)
                                if data[j+1]==" " and data[x-2:x]=="  ":
                                    output+=data[j+2:x-2]+'|'                            
                                elif data[j+1]==" " and data[x-1]==" ":
                                    output+=data[j+2:x-1]+'|'
                                else:
                                    output+=data[j+1:x]+'|'
                                break;
                        break;
            if data[i+1:i+4]=="/tr":
                output=output[:len(output)-1]
                output+="\n"
    return output
#Function to write the given data into a file called output.csv
def csv_create(content):
    with open(os.path.dirname(__file__)+"\\output.csv", 'wt') as f:
        f.write(content)
csv_data = parse(get_input())
csv_create(csv_data)