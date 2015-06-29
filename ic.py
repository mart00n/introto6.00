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

#def f1(x):
#    def g():
#        x = 'abc'
#        assert False
#    x = x + 1
#    print('x =', x)
#    g()
#    return x
#
#x = 3
#z = f1(x)
#
#def isEven(i):
#    # assumes i is a positive int
#    # returns True if i is even, otherwise returns false
#    return i % 2 == 0

#x = 100
#divisors = ()
#for i in range(1, x):
#    if x % i == 0:
#        divisors = divisors + (i,) # note the , is to define i as part of a tuple
#print(divisors)
#
#Techs = ['MIT', 'Cal Tech']
#Ivys = ['Harvard', 'Yale', 'Brown']
#Univs = []
#Univs.append(Techs)
#print('Univs =', Univs)
#
#Univs.append(Ivys)
#print('Univs =', Univs)
#for e in Univs:
#    print('e =', e)
#
#Flat = Techs + Ivys
#print(Flat)
#for x in Flat:
#    print(x)
#
#artSchools = ['RISD', 'Harvard']
#for u2 in artSchools:
#    if u2 in Flat:
#        Flat.remove(u2)
#
#print('Flat =', Flat)
#
#Flat.sort()
#print('Flat =', Flat)
#
#Flat[1] = 'UMass'
#print('Flat =', Flat)

#L1 = [2]
#L2 = [L1, L1]
#print('L2 =', L2)
#
#L1[0] = 3
#print('L2 =', L2)
#
#L2[0] = 'a'
#print('L2 =', L2)
#
#L1 = [2]
#print('L2 =', L2)
#L2 = L1
#L2[0] = 'a'
#print('L1 =', L1)
#print('L2 =', L2)

#def copyList(LSource, LDest):
#    for e in LSource:
#        LDest.append(e)
#        print('LDest =', LDest)
#L1 = []
#L2 = [1, 2, 3]
#copyList(L2, L1)
#print(L1)
#print(L2)
#
##copyList(L1, L1) # creates an infinite loop! LSource and LDest both point to the same object
##print(L1)

#D = {1: 'one', 'deux': 'two', 'pi': 3.14159}
#D1 = D
#print(D1)
#D[1] = 'uno'
#print(D1)
#for k in D1.keys():
#    print(k, '=', D1[k])

#EtoF = {'bread': 'du pain', 'wine': 'du vin',\
#        'eats': 'mange', 'drinks': 'bois',\
#        'likes': 'aime', 1: 'un',\
#        '6.00': '6.00'}
#
#def translateWord(word, dictionary):
#    if word in dictionary:
#        return dictionary[word]
#    else:
#        return word
#
#def translate(sentence):
#    translation = ''
#    word = ''
#    for c in sentence:
#        if c != ' ':
#            word = word + c
#        else:
#            translation = translation + ' '\
#                          + translateWord(word, EtoF)
#            word = ''
#    return translation[1:] + ' ' + translateWord(word, EtoF)
#    # the extra term above is because sentences do not end with a ' '
#
#print(translate('John eats bread'))
#print(translate('Steve drinks wine'))
#print(translate('John likes 6.00'))

def simpleExp(b, n):
    if n == 0:
        return 1
    else:
        return b * simpleExp(b, n - 1)
#example uses recursion to find an exponent

#print(simpleExp(4, 4))

def hanoi(n, f, t, s):
    """
    Solves variants of the Tower of Hanoi Problem recursively
    n is stack size, f is from stack, t is to stack, s is spare stack
    """
    if n == 1:
        print('Move from', f, 'to', t)
    else:
        hanoi(n-1, f, s, t)
        hanoi(1, f, t, s)
        hanoi(n-1, s, t, f)

#hanoi(6, 'one', 'two', 'three') #64 discs would take millions of years to calculate...

def toChars(s): # this doesn't work because fuck python 2...
    import string
    s = string.lower(s)
    ans = ''
    for c in s:
        if c is string.lowercase:
            ans = ans + c
    return ans

def isPalindrome(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and isPalindrome(s[1:-1])

print(isPalindrome('able was I ere I saw elba'))

def fib(n):
    # make a recursive fibonnaci later, can't see this guy's shit

#TEST
