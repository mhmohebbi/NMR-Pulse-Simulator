"""
Created on August 2nd, 2019
@author: hossein.mohebbi
"""

# Import necessary modules
import csv


def read_csv(file_name_str):
    vals = []
    # opening correct file
    with open(file_name_str, 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            vals.append(row)
    csvFile.close()
    return vals


"""TEST"""
#x = read_csv('data')
#print x