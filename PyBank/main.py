
## Importing Prerequisites 
import os
import csv

datapath = os.path.join('', 'Resources', 'budget_data.csv')

with open(datapath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    ## Read first row and move to next
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)