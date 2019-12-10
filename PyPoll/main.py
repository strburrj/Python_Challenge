import os
import csv

csvpath = os.path.join("/Users/strawberrymeow/Desktop/My_Class_Repo/Python_Challenge/PyPoll/Resources/election_data.csv")

total_votes = 0
candidates = []
number_of_votes = []

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header=next(csvreader)
    row=next(csvreader)
    total_votes = total_votes + 1

    row=next(csvreader)
    total_votes = total_votes + 1
    

    for row in csvreader:
        total_votes = total_votes + 1

print(f"Election Results")
print(f"------------------")


    

       
