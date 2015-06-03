# Problem Set 1
# Name: mart00n
# Collaborators:
# Time Spent:
#
# Program calculates credit card payments over 1 year and presents the user with summary information
bal = float(input('Please enter the current balance on your account: '))
int_rate = float(input('Please enter your annual interest rate (as a decimal, ex. 20% = 0.2): '))
min_rate = float(input('Please enter the minimum monthly payment rate (as a decimal, ex. 2% = 0.02): '))
total_paid = 0

for i in range(1,13):
    minpay = bal * min_rate
    int_paid = int_rate / 12 * bal
    principle_paid = round(minpay, 2) - round(int_paid, 2)
    bal = round(bal, 2) - principle_paid
    total_paid += minpay
    print('Month:', i)
    print('Minimum monthly payment: $', round(minpay, 2))
    print('Principle paid: $', round(principle_paid, 2))
    print('Remaining balance: $', round(bal, 2))
    print()

print('RESULT')
print('Total amount paid: $', round(total_paid, 2))
print('Remaining balance: $', round(bal, 2))

