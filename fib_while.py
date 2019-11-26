n = int(input('\nEnter number up to which fibonacci series will be printed.\n\nn = '))

fib_list=[1,1]

a=1
b=1

print(a,b,end=' ')

while(a+b<=n):
    fib_list.append(a+b)
    print(a+b,end=' ')
    a,b=b,a+b

print('\nlist of the same is: {}\n'.format(fib_list))
