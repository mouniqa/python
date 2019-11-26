# lcm of two numbers

def lcm(a,b):
    l=0
    min=0
    max = 0
    if(a>b):
        l=a
        min = b
        max = a
    elif(b>a):
        l=b
        min = a
        max = b
    else:
        return a
    while(max%min != 0):
        max = max+l
    return max

if(__name__=='__main__'):
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))

    print(lcm(a,b))
