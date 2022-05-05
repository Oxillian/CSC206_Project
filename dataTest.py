import csv

def checkNum(string):
    try:
        i=int(string)
    except:
        return True
    if (string== "  "):
        return True
    return False 
listed=[]
usaList=[]
csvFile='./richathletes.csv'
with open(csvFile) as file:
    #file=open(csvFile)
    reader = csv.reader(file, csv)
    for row in reader:
        previousYearRank=0
        
        if checkNum(row[3]):
            #list.append(row)
            previousYearRank=-1
        else:
            previousYearRank=row[3]
        listed.append(row)

        if row[1]=='USA':
            usaList.append(row)
            print(usaList)
        

    #print(listed[2][2])
