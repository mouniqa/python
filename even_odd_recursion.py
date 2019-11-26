number = int(input('Enter number: '))

def even_odd(n):
    if n<2:
        return (n%2==0)
    else:
        return even_odd(n-2)

if even_odd(number) == True:
    print('\nEven number\na')
else:
    print('\nOdd number\n')
