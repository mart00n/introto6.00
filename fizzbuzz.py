# Write a program that prints the numbers from 1 to 100. But for multiples of three print "Fizz"
# instead of hte number and for multiples of five print "Buzz". For numbers which are multiples of
# both three and five print "FizzBuzz".

for i in range(1,101):
    s = str(i)
    if i % 3 == 0 or i % 5 == 0:
        s = ''
        if i % 3 == 0:
            s += 'Fizz'
        if i % 5 == 0:
            s += 'Buzz'
    print(s)

