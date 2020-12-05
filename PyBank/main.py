#PyBank
#Your task is to create a Python script that analyzes the records to calculate each of the following:
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period
#In addition, your final script should both print the analysis to the terminal and export a text file with the results.




#Import necessary dependencies 
import os
import csv

#Path to collect data from the Resources folder
pybank_csv = os.path.join('OneDrive', 'Desktop', 'python-challenge', 'PyBank',  'Resources', 'pybank.csv')


data = []
with open(pybank_csv, 'r') as csvfile:
    #Split the data on comas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    #Loop through the data
    for row in csvreader:
        date = row[0]
        profit = int(row[1])
        data.append([date, profit])


# Calculate total months
total_month = total_months + 1

#Calculate the net total
net_total = net_total + int(row[1])

#Calculate the net total
net_total = net_total + int(row[1])

#Calculate change in profit
profit_change = int(row[1]) - previous_value

checker = {}
total = 0
for row in data:
    date = row[0]
    profit = row[1]
    total = total + profit

    if date not in checker:
        checker[date] = True
 print(len(checker.keys()
 print(total)

changes = []
for i in range(len(data) - 1):
    changes.append(data[i][1] - data[i + 1][1])
print(sum(changes)/len(changes))

#set format for printing
output = (
    f"Financial Analysis \n"
    f"------------------ \n"
    f"Total Months: {total_votes} \n"
    f"Average Change: {average_change} \n"
    f"Greatest Increase in Profits: {greatest_increase} \n"
    f"Greatest Decrease in Profits: {greatest_decrease}
)

#Output
print(output)
with open("analysis/output.txt", "w") as txt_file:
    txt_file.write(output)

