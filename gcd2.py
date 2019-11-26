def gcd(a,b):
    if(a==b):
        return a
    if(a<b):
        a,b=b,a
    gcd = b
    while(a%b != 0):
        print(a,b)
        gcd = a%b
        a=b
        b=gcd
    return gcd

a=int(input('Enter a: '))
b=int(input('Enter b: '))

print(gcd(a,b))
