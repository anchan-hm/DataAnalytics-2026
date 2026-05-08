# creating "while" loop to reach savings goal

# calculating values (can change whenever)
balance = 100
savings_goal = 400
weekly_save = 100

# using "while" loop to reach goal
while balance < savings_goal:
    if balance >= savings_goal * 0.50 and balance < savings_goal * 0.75:  #more than halfway
        balance += weekly_save #adding to balance
        print("Almost there! This week my balance is up to", balance)

    elif balance >= savings_goal * 0.75: #at least 75%
        balance += weekly_save
        print("So close! After treating myself, my balance is up to", balance)

    else:  #adding weekly and not hitting goal marks
        balance += weekly_save
        print("This week my balance increased to", balance)

# final print for loop completion
print("Goal met! My current balance is", balance)
#output: This week my balance increased to 200
#        Almost there! This week my balance is up to 300
#        So close! After treating myself, my balance is up to 400
#        Goal met! My current balance is 400