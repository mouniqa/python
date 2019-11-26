 # factorial of n

number = int(input('Enter the number: '))

factorial = 1
print(number,end='')
while(number>1):
    print(' * {}'.format(number-1),end='')
    factorial *= number
    number -= 1

print(' =',factorial)
print('factorial is : ',factorial)
