#x = int(input('Enter a number: '))
#if x % 2 == 0:
#    print('even')
#else:
#    print('odd')
#    if x % 3 != 0:
#        print('and not divisible by 3')

# Find the cubic root of a perfect cube program
x = int(input('Enter an integer: '))
ans = 0
while ans ** 3 < abs(x):
    ans = ans + 1
    #this is a debugging print line you can uncomment
    #print('current guess = ', ans)
if ans ** 3 != abs(x):
    print(x, 'is not a perfect cube.')
else:
    if x < 0:
        ans = -ans
    print('Cubic root of ' + str(x) + ' is ' + str(ans))

