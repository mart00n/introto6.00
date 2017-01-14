# mart00n
# 10/9/2016

balance = float(input('Enter initial balance:'))
minrate = float(input('Enter your monthly minimum payment rate:'))
intrate = float(input('Enter your annual interest rate:'))
months = 12

for i in range(1, 12 + 1):
    minpay = minrate * balance
    intpaid = intrate / months * balance
    prinpaid = minpay - intpaid
    balance += -prinpaid
    print('Month:', i)
    print('Minimum monthly payment: $', minpay)
    print('Principle paid: $', prinpaid)
    print('Remaining balance: $', balance)

