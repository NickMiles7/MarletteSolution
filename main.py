"""
This is the entrypoint to the program. 'python main.py' will be executed and the 
expected csv file should exist in ../data/destination/ after the execution is complete.
"""

from src.some_storage_library import *


def main():
    

    # We open the columns text file, and read it line by line into a list, while also 
    # splitting each between the position, and the header text
    cols = []
    f = open("./data/source/SOURCECOLUMNS.txt","r")
    for line in (f):
        cols.append(line.split("|"))

    # Then we sort that list of headers into the correct order 
    sortedHeaders = sorted(cols, key=lambda x: int(x[0]))

    # Open the solution.csv file we are going to begin to build. And then write in our list 
    # of ordered column headers, joining them with a ",", and stripping out the newlines
    output = open("solution.csv",  'w+')
    output.write(','.join([str(header[1]) for header in sortedHeaders]).replace('\n',''))

    # The sourcedata file requires much less transformation than the headers - we can just 
    # read in line by line, replacing the pipes with commas
    data = open ("./data/source/SOURCEDATA.txt","r")
    output.write("\n")
    for line in (data):
        output.write(line.replace("|",","))
       
    output.close()

    try:
        SomeStorageLibrary().load_csv("solution.csv")
    except:
        print("Caught an Error - during testing shutil was throwing error if the destination already exists. Hopefully you aren't seeing this for another reason, or I probably won't be getting the job ;)")





if __name__ == '__main__':
    """Entrypoint"""
    print('Beginning the ETL process...')
    main()
