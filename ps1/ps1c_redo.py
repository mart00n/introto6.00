# mart00n
# 10/09/2016

eps = 0.01
bal = float(input('Enter balance: '))
intrate = float(input('Enter your annual interest rate: '))
monthrate = intrate / 12.0
low = bal / 12.0
hi = (bal * (1.0 + monthrate) ** 12.0) / 12.0
loopbal = bal
payment = (hi - low) / 2.0

while abs(loopbal) >= eps:
    for i in range(1,13):
        loopbal = loopbal * (1.0 + monthrate) - payment
    if loopbal < -eps:
        hi = payment
        loopbal = bal
        payment = (hi - low) / 2.0 + low
    elif loopbal > eps:
        low = payment
        loopbal = bal
        payment = (hi - low) / 2.0 + low
    else:
        break 

print('Pay', payment, 'per month to pay off your debt within 1 year.')


