def lcm(a,b):
    if(a==b):
        return a
    if(a<b):
        a,b=b,a
    lcm=a
    while(a%b!=0):
        lcm=lcm+a

    return lcm

if(__name__=='__main__'):
    a=int(input('Enter a: '))
    b=int(input('Enter b: '))
    print(lcm(a,b))
