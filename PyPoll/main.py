

## Importing Prerequisites 
import os
import csv

datapath = os.path.join('','Resources','election_data.csv')


with open(datapath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    ## Read first row and move to next
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    #create list from scv file

    candidateList = []
    candidateScore = []
    candidateHeader = ['Name', 'Score']
    recordCounter = 0 
    for row in csvreader:
        counter = 0
       
        for field in row:
            
            #print(field)
            if (counter == 2 and  field not in candidateList):
                #print(field)
                candidateList.append(field)
                candidateScore.append(1)
                recordCounter +=1
            elif (counter == 2 and field in candidateList):
                #print (counter)
                #print (candidateList.index(field))
                candidateScore[candidateList.index(field)] = int(candidateScore[candidateList.index(field)]) + 1
                recordCounter +=1
            counter +=1
    #print(candidateList)
    #print(candidateScore)

    zipObj = zip(candidateList, candidateScore)

    Candidates = dict(zipObj)
    listofTuples = sorted(Candidates.items() , reverse = True,  key=lambda x: x[1])

    print ('Election Results')
    print ('------------------------------------------------------')

    for elem in listofTuples:
        print(elem[0] , " ::" , elem[1] ,'::', (format (elem[1] / recordCounter, '0.00%')))
    print ('------------------------------------------------------')
    print ('The Winner is :' ,(listofTuples[0][0]))
    
   
   
output_path = os.path.join("", "Resources", "Candidates.csv")
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer (csvfile, delimiter=',')
    for elem in listofTuples:
        csvwriter.writerow(elem)

  
    


