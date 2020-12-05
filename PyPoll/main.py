#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.
#In addition, your final script should both print the analysis to the terminal and export a text file with the results.

import os
import csv
import operator
from collections import defaultdict

#Path to csv data
pypoll_csv = os.path.join('Resources', 'pypoll.csv')

#Define variables
total_votes = 0
candidate_votes = {}
candidate_votes_percentage = {}
combined_votes_percentage = defaultdict(list)
candidates = []
percentage = 0
winner_name = []

#Read csv file
with open(pypoll_csv) as csvfile:

    #Split the data on the commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    header = next(csvreader)

    #Loop through the data
    for row in csvreader:

        #Calculate total votes cast
        total_votes = total_votes + 1

        name = row[2]

        #Calculate the total votes each candidate won
        if name not in candidate_votes:
            candidate_votes[name] = 1
        else:
            if candidate_votes[name] == 1:
                candidates.append(name)
                candidate_votes[name] += 1
            else:
                candidate_votes[name] += 1

#Calculate the percentage of votes each candidate won and 
candidate_votes_percentage = dict(candidate_votes)

vote_res = " "
for key, value in candidate_votes_percentage.items():
    vote_percentage = float(value)/float(total_votes) * 100
    vote_res += key + ' ' + f'{vote_percentage:.3f}% ({value})\n'


#Determine winner of the election 
winner_name = max(candidate_votes.items(), key=operator.itemgetter(1))[0]

#set format for printing
output = (
    f"Election Results \n"
    f"------------------ \n"
    f"Total Votes: {total_votes} \n"
    f"------------------ \n"
    f"{vote_res} \n"
    f"------------------ \n"
    f"Winner {winner_name} \n"
    f"------------------ \n"
)

#Output
print(output)
with open("analysis/output.txt", "w") as txt_file:
    txt_file.write(output)