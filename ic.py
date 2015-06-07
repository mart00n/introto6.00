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
#x = 0.5
#eps = 0.01
#guesses = 0
#low = 0.0
#high = max(x, 1.0)
#ans = (high + low)/2.0
#while abs(ans ** 2 - x) >= eps and ans <= x:
#    print('Low:',low,'High:', high,'Guess:', ans)
#    guesses += 1
#    if ans ** 2 < x:
#        low = ans
#    else:
#        high = ans
#    ans = (high + low)/2.0
#print('# of guesses = ', guesses)
#print(ans, 'is close enough to square root of', x)

# New program with functions
#def within_eps(x, y, epsilon):
#    #x, y, eps floats, eps > 0.0
#    #returns True if x is within eps of y
#    return abs(x - y) <= eps

#def f(x):
#    x = x + 1
#    print('x =', x)
#    return x

#print(within_eps(2, 3, 1))
#val = within_eps(2, 3, 0.5)
#print(val)

#x = 3
#z = f(x)
#print('z =', z)
#print('x =', x)

def f1(x):
    def g():
        x = 'abc'
        assert False
    x = x + 1
    print('x =', x)
    g()
    return x

x = 3
z = f1(x)

def isEven(i):
    # assumes i is a positive int
    # returns True if i is even, otherwise returns false
    return i % 2 == 0
