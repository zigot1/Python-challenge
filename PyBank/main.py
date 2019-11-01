
## Importing Prerequisites 
import os
import csv

datapath = os.path.join('', 'Resources', 'budget_data.csv')

profitloss = 0.0

with open(datapath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    ## Read first row and move to next
    csv_header = next(csvreader)
    #create list from scv file
    rows = list(csvreader)
    ###print(f"CSV Header: {csv_header}") control print
    startingValue = float(rows[0][1])
    changes = 0
    comp = 0
    compMaxT = 0
    compMinT = 0
    profitloss = float(rows[1][1])
    for x in range (0, len(rows)-1):
        profitloss = profitloss + float(rows[x+1][1])
        changes = changes + (float(rows[x+1][1]) - float(rows[x][1]))
        ### print (changes , ':::', x) --- control print
        if startingValue < float(rows[x][1]):
            comp = float(rows[x][1]) - startingValue
            if compMaxT < comp:
                compMaxT = comp
                MaxDate = rows[x][0]
                MaxProfit = float(rows[x][1]) - float(rows[x-1][1])
        elif startingValue > float(rows[x][1]):
            comp = startingValue - float(rows[x][1])
            if compMinT < comp:
                compMinT = comp
                MinDate = rows[x][0]
                MinProfit = float(rows[x][1]) - float(rows[x-1][1])
    
print ('Financial Analysis')
print ('------------------------------------------------------')
print(f'Total months                    :', len(rows))
print(f'Total                           :$',profitloss)
print(f'Average Change                  :$', changes / (len(rows)-1))
print(f'Greatest Increase in Profits    :$',  MaxDate , '...:$',MaxProfit)
print(f'Greatest Decrease in Profits    :$',  MinDate , '...:$',MinProfit)

findingHeaders = ['Total months','Total','Average Change','Greatest Increase in Profits','Increase Value','Greatest Decrease in Profits','Decrease Value']
findingsValues = [len(rows),profitloss,changes / (len(rows)-1),MaxDate,MaxProfit,MinDate,MinProfit]

output_path = os.path.join("", "Resources", "Output.csv")
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(findingHeaders)

    # Write the second row
    csvwriter.writerow(findingsValues)