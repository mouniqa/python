# prints fiboncci sereis up to n
n=int(input('Enter the number upto which fibonacci series will be printed.\n\tn = '))
fib_list = [1,1]
a=1
b=1
print(a,b,end=' ')
def fibonacci(a,b):
    if(a+b<=n):
        fib_list.append(a+b)
        print(a+b,end=' ')
        fibonacci(b,a+b)
    else:
        print()
        return
fibonacci(a,b)
print('\nfib_list is: {}\n'.format(fib_list))
