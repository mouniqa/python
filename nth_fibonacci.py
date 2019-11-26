# This program will give you the nth fibonacci number

n = int(input('\nEnter n = '))

def fib(n):
    nth_fib = 1
    count = 2
    a=1
    b=1
    if n>2:
        while(count!=n):
            count += 1
            nth_fib = a+b
            a,b = b,a+b

    return nth_fib

print('nth fibonacci number is: {}'.format(fib(n)))
