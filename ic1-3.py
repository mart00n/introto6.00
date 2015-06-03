# Simple if else example
#x = int(input('Enter a number: '))
#if x % 2 == 0:
#    print('even')
#else:
#    print('odd')
#    if x % 3 != 0:
#        print('and not divisible by 3')

# Find the cubic root of a perfect cube program
#x = int(input('Enter an integer: '))
#ans = 0
#while ans ** 3 < abs(x):
#    ans = ans + 1
#    #this is a debugging print line you can uncomment
#    print('current guess = ', ans)
#if ans ** 3 != abs(x):
#    print(x, 'is not a perfect cube.')
#else:
#    if x < 0:
#        ans = -ans
#        print('You entered a negative number.')
#    print('Cubic root of ' + str(x) + ' is ' + str(ans))

# This version of the program does the same with a for loop
#x = int(input('Enter an integer: '))
#for ans in range(0, abs(x) + 1):
#    if ans ** 3 == abs(x):
#        break
#if ans ** 3 != abs(x):
#    print(x, 'is not a perfect cube')
#else:
#    if x < 0:
#        ans = -ans
#    print('Cube root of ' + str(x) + ' is ' + str(ans))

# This program will do non integer values and can solve non-perfect square roots
#x = 563
#eps = 0.01
#numguesses = 0
#ans = 0.0
#while abs(ans**2 - x) >= eps and ans <= x: # Note decrementing function here
#    ans += 0.0001
#    numguesses += 1
#print('numguesses = ', numguesses)
#if abs(ans ** 2 - x) >= eps:
#    print('Failed on square root of ', x)
#else:
#    print(ans, 'is close enough to the square root of ', x)

# Bisection search version of program
x = 12345.0
eps = 0.01
guesses = 0
low = 0.0
high = x
ans = (high + low)/2.0
while abs(ans ** 2 - x) >= eps and ans <= x:
    print(low, high, ans)
    guesses += 1
    if ans ** 2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('# of guesses = ', guesses)
print(ans, 'is close enough to square root of', x)
# Note: Answer to prof question is values between 0 and 1 will not be found by this method
