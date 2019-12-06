# Import Libraries
import os
import csv

#Where am I
print('You are here!!!')
print(os.getcwd())

# path to file
csvpath = os.path.join('Resources','election_data.csv')

# Declaring the Variables 
total_votes = 0
candidates = {}
candidates_percent = {}
winner_count = 0
winner = ""

# Read the File
with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader, None)
    for row in csvreader:
        #total votes
        total_votes += 1
        #total candidates
        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

        # percentages
        for key, value in candidates.items():
            candidates_percent[key] = round((value/total_votes) * 100, 1)

        # winner
        for key in candidates.keys():
            if candidates[key] > winner_count:
                winner = key
                winner_count = candidates[key]


# Print to terminal
print("Election Results")
print("-------------------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------------------")
for key, value in candidates.items():
    print(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ")")
print("-------------------------------------")
print("Winner: " + winner)
print("-------------------------------------")


# writing the new file
newfile = "analysis.txt"
with open(newfile, 'w') as txtfile:
    txtfile.write("Election Results \n")
    txtfile.write("------------------------------------- \n")
    txtfile.write("Total Votes: " + str(total_votes) + "\n")
    txtfile.write("------------------------------------- \n")
    for key, value in candidates.items():
        txtfile.write(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ") \n")
    txtfile.write("------------------------------------- \n")
    txtfile.write("Winner: " + winner + "\n")
    txtfile.write("------------------------------------- \n")