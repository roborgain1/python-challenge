import os
import csv
import sys

count = 0
kCount = 0
cCount = 0
lCount = 0
oCount = 0

candidateList = []
csvpath = os.path.join("Resources/election_data.csv") 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        count += 1
        if row[2] not in candidateList:
            candidateList.append(row[2])
        if row[2] == "Khan":
            kCount += 1
        elif row[2] == "Correy":
            cCount += 1
        elif row[2] == "Li":
            lCount += 1
        elif row[2] == "O'Tooley":
            oCount += 1
    if kCount > cCount and kCount > lCount and kCount > oCount:
        winner = "Winner: Khan"
    elif cCount > kCount and cCount > lCount and cCount > oCount:
        winner = "Winner: Correy"
    elif lCount > kCount and lCount > cCount and lCount > oCount:
        winner = "Winner: Li"
    elif oCount > kCount and oCount > cCount and oCount > lCount:
        winner = "Winner: O'Tooley"

print("Election Results")
print("-"*40)
print("Candidates:", candidateList[0] + ",", candidateList[1] + ",", candidateList[2] + ",", candidateList[3])
print("-"*40)
print("Total Votes:", count)
print("-"*40)
kPercent = round(((kCount/count)*100), 2)
print("Khan:", str(kPercent) + "%", "(" + str(kCount) + ")")
cPercent = round(((cCount/count)*100), 2)
print("Correy:", str(cPercent) + "%", "(" + str(cCount) + ")")
lPercent = round(((lCount/count)*100), 2)
print("Li:", str(lPercent) + "%", "(" + str(lCount) + ")")
oPercent = round(((oCount/count)*100), 2)
print("O'Tooley:", str(oPercent) + "%", "(" + str(oCount) + ")")
print("-"*40)
print(winner)
print("-"*40)

stdoutOrigin=sys.stdout 
txtPath = os.path.join("Analysis/election_analysis.txt")
sys.stdout = open(txtPath, "w")

print("Election Results")
print("-"*40)
print("Candidates:", candidateList[0] + ",", candidateList[1] + ",", candidateList[2] + ",", candidateList[3])
print("-"*40)
print("Total Votes:", count)
print("-"*40)
kPercent = round(((kCount/count)*100), 2)
print("Khan:", str(kPercent) + "%", "(" + str(kCount) + ")")
cPercent = round(((cCount/count)*100), 2)
print("Correy:", str(cPercent) + "%", "(" + str(cCount) + ")")
lPercent = round(((lCount/count)*100), 2)
print("Li:", str(lPercent) + "%", "(" + str(lCount) + ")")
oPercent = round(((oCount/count)*100), 2)
print("O'Tooley:", str(oPercent) + "%", "(" + str(oCount) + ")")
print("-"*40)
print(winner)
print("-"*40)

sys.stdout.close()
sys.stdout=stdoutOrigin