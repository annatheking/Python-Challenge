import csv

bank = "/Users/shuashua/Documents/Data_Analytic_Boot_Camp/Homework3/python-challenge/PyBank/03_python_homework_Instructions_PyBank_Resources_budget_data.csv"

with open(bank, newline="", encoding="UTF-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader,None)

    net = 0

    for row in csvreader: 
        pos_num = row[1].split("-")

    #The total number of months included in the dataset
         

    #The total net amount of "Profit/Losses" over the entire period
        if pos_num[0] == '':
            net -= int(pos_num[1])
            #print(pos_num[1])
        else:
            net += int(pos_num[0])
            #print(pos_num[0])

    #The average change in "Profit/Losses" between months over the entire period


    #The greatest increase in profits (date and amount) over the entire period


    #The greatest decrease in losses (date and amount) over the entire period


print("Financial Analysis")
print("----------------------------")    
print(f"Total: ${net}")