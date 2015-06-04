# Problem Set 1: Problem 2
# Name: mart00n
# Collaborators:
# Time Spent: ~ 50m
#
# Problem 2: Program calculates a fixed monthly payment that will eliminate balance in year
# Note: only finds payment to a multiple of $10
initial_bal = float(input('Please enter the current balance on your account: '))
int_rate = float(input('Please enter your annual interest rate (as a decimal, ex. 20% = 0.2): '))
#min_rate = float(input('Please enter the minimum monthly payment rate (as a decimal, ex. 2% = 0.02): '))
total_paid = 0
payment = 10.0
monthly_int = int_rate / 12
bal = initial_bal

while bal > 0:
    for i in range(1,13):
        bal = round(bal * (1 + monthly_int), 2) - payment
        #total_paid += payment
        if bal <= 0:
            break
    if bal > 0:
        bal = initial_bal
        payment += 10.0
    
print('RESULT')
#print('Total amount paid: $', round(total_paid, 2))
print('Monthly payment to pay off debt in 1 year: $', payment)
print('Number of months needed:', i)
print('Remaining balance: $', round(bal, 2))
