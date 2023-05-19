import os
import csv

# CSV file
csvpath = os.path.join('python-challenge/PyBank/Resources/budget_data.csv')

# Initialize variables
totalMonths = 0
netTotal = 0
previousProfitLoss = 0
profitLossChangeList = []
greatestIncrease = ["", 0]
greatestDecrease = ["", 9999999999]

# Read the CSV file 
with open(csvpath, newline="") as csvfile:
    csvReader = csv.reader(csvfile, delimiter=",")
    header = next(csvReader)

# Iterate over each row
    for row in csvReader:
        # Getting total months
        totalMonths += 1

        # Calculate the net total amount of "Profit/Losses"
        netTotal += int(row[1])

        # Calculate the change in profit/loss
        profitLossChange = int(row[1]) - previousProfitLoss
        previousProfitLoss = int(row[1])

        # Append the profit/loss change to the list
        profitLossChangeList.append(profitLossChange)

        # greatest increase in profits
        if profitLossChange > greatestIncrease[1]:
            greatestIncrease[0] = row[0]
            greatestIncrease[1] = profitLossChange

        # Find the greatest decrease in profits
        if profitLossChange < greatestDecrease[1]:
            greatestDecrease[0] = row[0]
            greatestDecrease[1] = profitLossChange

# Calculate the average change
averageChange = sum(profitLossChangeList) / len(profitLossChangeList)

# Format the results as strings
totalMonthsStr = str(totalMonths)
netTotalStr = "${:,.2f}".format(netTotal)
averageChangeStr = "${:,.2f}".format(averageChange)
greatestIncreaseStr = greatestIncrease[0] + " $(" + "{:,.2f}".format(greatestIncrease[1]) + ")"
greatestDecreaseStr = greatestDecrease[0] + " $(" + "{:,.2f}".format(greatestDecrease[1]) + ")"

# Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print("Total Months:", totalMonthsStr)
print("Total:", netTotalStr)
print("Average Change:", averageChangeStr)
print("Greatest Increase in Profits:", greatestIncreaseStr)
print("Greatest Decrease in Profits:", greatestDecreaseStr)

# Export the analysis as a text file
output_path = os.path.join("python-challenge/PyBank/analysis/analysis.txt")

with open(output_path, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write("Total Months: " + totalMonthsStr + "\n")
    txtfile.write("Total: " + netTotalStr + "\n")
    txtfile.write("Average Change: " + averageChangeStr + "\n")
    txtfile.write("Greatest Increase in Profits: " + greatestIncreaseStr + "\n")
    txtfile.write("Greatest Decrease in Profits: " + greatestDecreaseStr + "\n")
