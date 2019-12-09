import os
import csv

csvpath = os.path.join("/Users/strawberrymeow/Desktop/My_Class_Repo/Python_Challenge/PyPoll/Resources/election_data.csv")

votes = 0
candidates = []
number_of_votes = []

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header=next(csvreader)
    row=next(csvreader)
    

    for row in csvreader:
        votes = votes + 1

        if row[2] not in candidates and row[2] not in "Candidate":
            candidates.append(row[2])
            
        elif row[2] in candidates and row [2] not in "Candidate":
                   





print(f"Election Results")
print(f"------------------")
print(f"Total Votes:" : str(votes))
print(f"------------------")
for count in range(len(candidates)):
    print(f"{candidates[count]}")
