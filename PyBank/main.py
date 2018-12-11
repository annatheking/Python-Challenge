import csv

bank = "/Users/shuashua/Documents/Data_Analytic_Boot_Camp/Homework3/python-challenge/PyBank/03_python_homework_Instructions_PyBank_Resources_budget_data.csv"

with open(bank, newline="", encoding="UTF-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader,None)

    profit_loss = []
    monthly_diff = []
    month_column = []

    net = 0
    mos = 0
    sum_monthly_diff = 0

    for row in csvreader: 
        month_column.append(row[0])

    #The total number of months included in the dataset
        mos += 1

    #The total net amount of "Profit/Losses" over the entire period
        pos_num = row[1].split("-")

        if pos_num[0] == '':
            net -= int(pos_num[1])
            profit_loss.append(-int(pos_num[1]))
        else:
            net += int(pos_num[0])
            profit_loss.append(int(pos_num[0]))

    #The average change in "Profit/Losses" between months over the entire period
    lead_profit_loss = profit_loss[0:(len(profit_loss)-1)]
    lag_profit_loss = profit_loss[1:len(profit_loss)]

    for i in range(mos-1):
        sum_monthly_diff += (lag_profit_loss[i] - lead_profit_loss[i])
        monthly_diff.append(lag_profit_loss[i] - lead_profit_loss[i])

    avg_diff = sum_monthly_diff / (mos-1)
    avg = round(avg_diff,2)

    #The greatest increase in profits (date and amount) over the entire period
    max_incrs = max(monthly_diff)
    position_incrs = monthly_diff.index(max_incrs) + 1
    item_incrs = month_column[position_incrs]

    #The greatest decrease in losses (date and amount) over the entire period
    max_decrs = min(monthly_diff)
    #print(max_decrs)
    position_decrs = monthly_diff.index(max_decrs) + 1
    item_decrs = month_column[position_decrs]

to_print = ("Financial Analysis\n"
            "----------------------------\n"   
            f"Total Months: {mos}\n"
            f"Total: ${net}\n"
            f"Average  Change: ${avg}\n"
            f"Greatest Increase in Profits: {item_incrs} ({max_incrs})\n"
            f"Greatest Decrease in Profits: {item_decrs} ({max_decrs})")

print(to_print)

with open("PyBankOutput.txt", "w") as text_file:
    text_file.write(to_print)