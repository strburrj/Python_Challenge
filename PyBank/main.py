import os
import csv

csvpath = os.path.join('/Users/strawberrymeow/Desktop/My_Class_Repo/Python_Challenge/PyBank/Resources/budget_data.csv')


total_months = 0
total_revenue = 0
total_revenue_change = 0
# prev_revenue = []
# greatest_inrev = []
# lowest_dcrev = [9999999999]

#revenue_change = []

with open(csvpath, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        header= next(csvreader)
        row = next(csvreader)
        total_months = total_months + 1
        current_rev=int(row[1])
        total_revenue = total_revenue + current_rev
        prev_revenue = current_rev

        row = next(csvreader)
        total_months = total_months + 1
        current_rev=int(row[1])
        total_revenue = total_revenue + current_rev
        monthly_change = current_rev - prev_revenue
        total_revenue_change = total_revenue_change + monthly_change

        greatest_inrev = monthly_change 
        lowest_dcrev = monthly_change

        prev_revenue = current_rev

        for row in csvreader:      

            total_months = total_months + 1

            current_rev=int(row[1])
            
            total_revenue = total_revenue + current_rev

           
            monthly_change = (current_rev) - prev_revenue
            prev_revenue = (current_rev)

            total_revenue_change = total_revenue_change + monthly_change

            #revenue_change.append(monthly_change)
            #average_revenue_change = round(sum(revenue_change)/total_months)

            if (monthly_change > greatest_inrev):
                #greatest_monthly = row [0]
                greatest_inrev = monthly_change

            if (monthly_change < lowest_dcrev):
                #lowest_monthly = row[0]
                lowest_dcrev = monthly_change

average_revenue_change = total_revenue_change / total_months

print("Financial Analysis")
print("-------------------")                   
print(f"Total Months: {total_months}")
print(f"Total Revenue: ${total_revenue}")
print(f"Average Revenue Change: ${average_revenue_change}")
print(f"Greatest Increase of Revenue: ${greatest_inrev}")
print(f"Greatest Decrease of Revenue: ${lowest_dcrev}")

#txtpath = os.path.join("Pybank/Summary_Analysis.txt")
txtpath = "/Users/strawberrymeow/Desktop/My_Class_Repo/Python_Challenge/PyBank/Summary_Analysis.txt"
with open(txtpath, 'w') as text_file:
    
    
    text_file.write(f"Financial Analysis\n")
    text_file.write(f'-----------------------------\n')
    text_file.write(f"Total Months: {total_months}\n")
    text_file.write(f"Total Revenue: ${total_revenue}\n")
    text_file.write(f"Average Revenue Change: ${average_revenue_change}\n")
    text_file.write(f"Greatest Increase in Revenue: ${greatest_inrev})\n")
    text_file.write(f"Greatest Decrease in Revenue: ${lowest_dcrev})\n") 

