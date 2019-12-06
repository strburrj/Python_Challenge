import os
import csv

csvpath = os.path.join("PyBank/budget_data.csv")


total_months = []
total_revenue = []
prev_revenue = []
greatest_inrev = []
lowest_dcrev = [9999999999]

revenue_change = []

with open(csvpath, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        for row in csvreader:        

            total_months = total_months + 1
            total_revenue = total_revenue + (int(row [1]))

            prev_revenue = (int(row [1]))
            monthly_change = (int(row [1])) - prev_revenue

            revenue_change.append(monthly_change)
            average_revenue_change = round(sum(revenue_change)/total_months)

            if (monthly_change > greatest_inrev):
                greatest_monthly = row [0]
                greatest_inrev = monthly_change

            if (monthly_change < lowest_dcrev):
                lowest_monthly = row[0]
                lowest_dcrev = monthly_change

print("Financial Analysis")
print("-------------------")                   
print(f"Total Months: {total_months}")
print(f"Total Revenue: ${total_revenue}")
print(f"Average Revenue Change: ${average_revenue_change}")
print(f"Greatest Increase of Revenue: ${greatest_inrev}")
print(f"Greatest Decrease of Revenue: ${lowest_dcrev}")

txtpath = os.path.join("Pybank/Summary_Analysis.txt")
with open(txtpath, 'w', newline='') as text_file:

    print("Financial Analysis", file=text_file)
    print('-----------------------------', file=text_file)
    print(f"Total Months: {total_months}", file=text_file)
    print(f"Total Revenue: ${total_revenue}", file=text_file)
    print(f"Average Revenue Change: ${average_revenue_change}", file=text_file)
    print(f"Greatest Increase in Revenue: ${greatest_inrev})", file=text_file)
    print(f"Greatest Decrease in Revenue: ${lowest_dcrev})",file=text_file) 

csvfile.close()