<<<<<<< HEAD
import os

# Module for reading CSV files
import csv
# The total number of votes cast
Total_votes=0
# A complete list of candidates who received votes
Candidate_list=[]
Candidate_Votes={}
# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote

csvpath = os.path.join( 'Resources', 'election_data.csv')




# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')


    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
   
    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        Total_votes +=1
        if row[2] not in Candidate_list:
            Candidate_list.append(row[2])
            Candidate_Votes[row[2]]=0
        Candidate_Votes[row[2]]+=1
Candidate_Percentages = {key:round( val / Total_votes*100,2) for key, val in Candidate_Votes.items()}
Winning_Candidate = max(Candidate_Votes, key=Candidate_Votes.get)
print(Total_votes)
print(Candidate_list)
print(Candidate_Votes)
print(Candidate_Percentages)
print(Winning_Candidate)
=======
Election Results 
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
>>>>>>> 30712ce9127bba057681a646d7e1f1be649d4043
