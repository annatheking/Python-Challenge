import csv

bank = "/Users/shuashua/Documents/Data_Analytic_Boot_Camp/Homework3/python-challenge/PyPoll/03_python_homework_Instructions_PyPoll_Resources_election_data.csv"

with open(bank, newline="", encoding="UTF-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader,None)

    total_vote = 0

    candidate = []

    for row in csvreader:
    #The total number of votes cast
        total_vote += 1
        candidate.append(row[2])

    #A complete list of candidates who received votes
    candidate_unique = list(set(candidate))

    #The total number of votes each candidate won
    #The percentage of votes each candidate won
    #The winner of the election based on popular vote.
    votes_per_person = [[float(round(candidate.count(i)*100/total_vote,3)), i, candidate.count(i)] for i in set(candidate)]
    votes_per_person.sort(reverse = True)

    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_vote}")
    print("-------------------------")
    for j in votes_per_person:
        print(f"{j[1]}: {j[0]}% ({j[2]})")
    print("-------------------------")

    