# find the smallest and biggest divisors for a given number (exclude 1 and number itself)

number = eval(input('Enter any number: '))

#below line crates a list of divisors of number using list comprehension
divisors = [x for x in range(1,number+1) if number%x==0]

print('list of all divisors of {} is {}'.format(number,divisors))

if len(divisors[1:-1])!=0:
    print('smalles divisor is --> ',min(divisors[1:-1]))
    print('biggest divisor is --> ',max(divisors[1:-1]))
else:
    print('The given number is prime number hence it will be devided by 1 and itself')
    print('smalles divisor is --> ',min(divisors))
    print('biggest divisor is --> ',max(divisors))
