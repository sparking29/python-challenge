#import file
import os
import csv

#Where am I
print('You are here!!!')
print(os.getcwd())

#path to file
budget_data = os.path.join('Instructions', 'PyBank', 'Resources', 'budget_data.csv')

#variables
total_months = 0
total_revenue = 0
monthly_change = []
month_count = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

#Read csv file
with open(budget_data, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)
    row = next(csvreader)

    previous_amount = int(row[1])
    total_months += 1
    total_revenue += int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]

    for row in csvreader:
        total_months += 1
        total_revenue += int(row[1])
        amount_change = int(row[1]) - previous_amount
        monthly_change.append(amount_change)
        previous_amount = int(row[1])
        month_count.append(row[0])
        
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]

        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]  

    #average and date
    average_change = sum(monthly_change)/ len(monthly_change)
    high = max(monthly_change)
    low = min(monthly_change)

#print stuff
print()
print(f"Financial Analysis")
print()
print(f"Total Months: {total_months}")
print(f"Total: ${total_revenue}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits:, {greatest_increase_month}, (${high})")
print(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${low})")

#write file
newfile = "analysis.txt"
with open(newfile, 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("-------------------------")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${total_revenue}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits:, {greatest_increase_month}, (${high})\n")
    txtfile.write(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${low})\n")
