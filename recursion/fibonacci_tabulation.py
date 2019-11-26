fib_list = {}

fib_list[1] = 1
fib_list[2] = 1



n = int(input('Enter any positive number: '))

for i in range(3,n+1):
    fib_list[i] = fib_list[i-1]+fib_list[i-2]

def fibonacci(n):
    return fib_list[n]

for i in range(1,n+1):
    print(i,':',fibonacci(i))
