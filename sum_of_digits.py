n = int(input('Enter any number: '))
digits=[]
while(n>0):
    digits.append(n%10)
    n=int(n/10)
print('The sum is: ',sum(digits))
