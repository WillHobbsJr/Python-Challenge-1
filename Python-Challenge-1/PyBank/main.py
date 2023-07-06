import os

# Module for reading CSV files
import csv
#The total number of months included in the dataset
Total_months=0
#The net total amount of "Profit/Losses" over the entire period
Total_Profit=[]
Total_Losses={}
#The changes in "Profit/Losses" over the entire period, and then the average of those changes

#The greatest increase in profits (date and amount) over the entire period

T#he greatest decrease in profits (date and amount) over the entire period

csvpath = os.path.join( 'Resources', 'budget_date.csv')




# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')


    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
   
    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        Total_profit +=1 
        if row[1] not in Total_Profit:
            Total_months
            Total_Profit 
            Total_Losses 
Budget_Increases = {key:round( val / Total_Profit*100,2) for key, val in Total_Profit.items()}
Budget_Decreases = max(Total_Losses, key=Total_Losses.get)
print(Total_months)
print(Total_Profit)
print(Total_Losses)
print(Budget_Increases) 
print(Budget_Decreases) 