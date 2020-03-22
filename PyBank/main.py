# Import os module & CSV files

import os
import csv

# Working directory

cwkdir = os.getcwd()

# Create and recognize the file path

filepath = os.path.join( cwkdir,'Resources','budget_data.csv')

# Variables

mcount = 0
total = 0
PreValue = 0
Diff = 0
DiffMax = 0
DiffMin = 0

# CSV file

with open(filepath, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     csv_header = next(csvreader)
     print(f'Financial Analysis'+'\n')
     print(f' ----------------------------'+'\n')
     for i in csvreader:
         month = i[0]
         Amount = i[1]
         iAmount = int(Amount)
         Diff =  iAmount - PreValue
         if DiffMax < Diff:
            DiffMax = Diff
            DiffMaxDate = month
         if DiffMin > Diff:
            DiffMin = Diff
            DiffMinDate = month

         PreValue = iAmount   
         mcount = mcount + 1
         total += int(Amount) 

# Print the results      

print(f'Total Months : {mcount}')
print(f'Total: $ {total}')
print(f'Greatest Increase in Profits: {DiffMaxDate} : ($ {DiffMax})')
print(f'Greatest Decrease in Profits: {DiffMinDate} : ($ {DiffMin})')