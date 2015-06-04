# Problem Set 1: Problem 3
# Name: mart00n
# Collaborators:
# Time Spent: ~40m 
#
# Problem : Program calculates a fixed monthly payment that will eliminate balance in year
# Note: rewritten to use bisection method, work to 0.01
initial_bal = float(input('Please enter the current balance on your account: '))
int_rate = float(input('Please enter your annual interest rate (as a decimal, ex. 20% = 0.2): '))
#min_rate = float(input('Please enter the minimum monthly payment rate (as a decimal, ex. 2% = 0.02): '))
total_paid = 0
monthly_int = int_rate / 12
bal = initial_bal
lopay = bal / 12.0
hipay = (bal * (1 + (int_rate / 12.0 )) ** 12.0) / 12.0
payment = (hipay - lopay) / 2.0 + lopay
#print(lopay, payment, hipay)

while 0.1 < abs(bal):
    for i in range(1,13):
        #print('foo')
        bal = round(bal * (1 + monthly_int), 2) - payment
        #total_paid += payment
    if bal > 0.1:
        bal = initial_bal
        lopay = payment
        payment = (hipay - lopay) / 2.0 + lopay
    elif bal < -0.1:
        bal = initial_bal
        hipay = payment
        payment = (hipay - lopay) / 2.0 + lopay
    else:
        break
            
print('RESULT')
#print('Total amount paid: $', round(total_paid, 2))
print('Monthly payment to pay off debt in 1 year: $', round(payment, 2))
print('Number of months needed:', i)
print('Remaining balance: $', round(bal, 2))
