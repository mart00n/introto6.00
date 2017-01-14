# mart00n
# 10/09/2016

bal = float(input('Enter balance: '))
intrate = float(input('Enter your annual interest rate: '))
monthrate = intrate / 12.0
payment = 10.0
loopbal = bal

while loopbal >= 0:
    for i in range(1,13):
        loopbal = loopbal * (1.0 + monthrate) - payment
        if loopbal <= 0:
            break
    if loopbal >= 0:
        payment += 10.0
        loopbal = bal
    else:
        print('Pay', payment, 'per month to pay off your debt within 1 year.')


