import csv

bank = "/Users/shuashua/Documents/Data_Analytic_Boot_Camp/Homework3/python-challenge/PyPoll/03_python_homework_Instructions_PyPoll_Resources_election_data.csv"

with open(bank, newline="", encoding="UTF-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader,None)

    total_vote = 0

    for row in csvreader:
    #The total number of votes cast
        total_vote += 1
        

    #A complete list of candidates who received votes


    #The percentage of votes each candidate won


    #The total number of votes each candidate won


    #The winner of the election based on popular vote.

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_vote}")
print("-------------------------")