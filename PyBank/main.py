import os
import csv
import sys 

count = 0
totalProfit = 0
sumChanges = 0 
previousValue = 0
totalValue = 0
maxProfit = 0
maxProfitDate = ""
maxLoss = 0
maxLossDate = ""

csvpath = os.path.join("Resources/budget_data.csv") 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        count += 1
        if count == 1:
            previousValue = int(row[1])
            totalProfit = int(row[1])
        else:
            if (int(row[1]) - previousValue) > maxProfit:
                maxProfit = int(row[1]) - previousValue
                maxProfitDate = row[0]
            if (int(row[1]) - previousValue) < maxLoss:
                maxLoss = int(row[1]) - previousValue
                maxLossDate = row[0]
            sumChanges += int(row[1]) - previousValue
            totalProfit += int(row[1])
            previousValue = int(row[1])

averageChanges = sumChanges/(count-1)
averageChanges = round(averageChanges, 2)
print("Financial Analysis")
print("-"*40)
print("Total Months:", count)
print("Total Profit: " + "$" + str(totalProfit))
print("Average Change: " + "$" + str(averageChanges))
print("Greatest Increase in Profits:", maxProfitDate, "(" + "$" + str(maxProfit) + ")")
print("Greatest Decrease in Profits:", maxLossDate, "(" + "$" + str(maxLoss) + ")")

stdoutOrigin=sys.stdout 
txtPath = os.path.join("Analysis/financial_analysis.txt")
sys.stdout = open(txtPath, "w")

print("Financial Analysis")
print("-"*40)
print("Total Months:", count)
print("Total Profit: " + "$" + str(totalProfit))
print("Average Change: " + "$" + str(averageChanges))
print("Greatest Increase in Profits:", maxProfitDate, "(" + "$" + str(maxProfit) + ")")
print("Greatest Decrease in Profits:", maxLossDate, "(" + "$" + str(maxLoss) + ")")

sys.stdout.close()
sys.stdout=stdoutOrigin

