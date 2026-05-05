# How do you calculate your net worth given your assets and debts?

# assets
# - car: $5,000
# - house: $200,000
# - savings: $8,000

# debts
# - student loans: $2,500
# - credit cards: $130
# - personal loans: $1,200

# formulas
car = 5000
house = 200000
savings = 8000

student_loans = 2500
credit_cards = 130
personal_loans = 1200

total_assets = car + house + savings #calculating assets
total_debts = student_loans + credit_cards + personal_loans #calculating debts

# net worth formula
net_worth = total_assets - total_debts

# displaying outputs
print("Your total assets are " + str(total_assets))
print("Your total debts are " + str(total_debts))
print("Your net worth is " + str(net_worth))