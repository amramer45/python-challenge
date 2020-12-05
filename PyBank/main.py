#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period
#In addition, your final script should both print the analysis to the terminal and export a text file with the results.

#Import dependencies 
import os
import csv

#Path to collect data from the Resources folder
pybank_csv = os.path.join('Resources', 'pybank.csv')

total_months = []
net_total = []
average_change = []

#Read csv
with open(pybank_csv) as csvfile:
    
    #Split the data on comas
    csvreader = csv.reader(csvfile, delimiter=',')

    #Skip the header
    header = next(csvreader)

    #Loop through the data
    for row in csvreader:

        total_months.append(row[0])
        net_total.append(int(row[1]))

#Change in profits/losses
for i in range(len(net_total) - 1):

    #Average change in profits/losses
    average_change.append(net_total[i + 1] - net_total[i])

#Greatest increase in profits/losses
greatest_increase = max(average_change)
greatest_increase_date = average_change.index(max(average_change)) + 1

#Greatest decrease in profits/losses
greatest_decrease = min(average_change)
greatest_decrease_date = average_change.index(min(average_change)) + 1

#set format for printing
output = (
    f"Financial Analysis \n"
    f"----------------------------- \n"
    f"Total Months: {len(total_months)} \n"
    f"Total: $ {sum(net_total)} \n"
    f"Average Change: $ {round(sum(average_change)/len(average_change), 2)} \n"
    f"Greatest Increase in Profits: {total_months[greatest_increase_date]} ($ {greatest_increase}) \n"
    f"Greatest Decrease in Profits: {total_months[greatest_decrease_date]} ($ {greatest_decrease}) \n"
)

#Output
print(output)
with open("analysis/output.txt", "w") as txt_file:
    txt_file.write(output)