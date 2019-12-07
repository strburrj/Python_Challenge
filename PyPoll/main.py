import os
import csv

csvpath = os.path.join("PyPoll/election-data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

total_months[]
