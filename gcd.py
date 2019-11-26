# GCD or HCF

def gcd(a,b):
  if (a<b):
      a,b = b,a
  if(a==0):
    return b
  else:
    print(a,b,a%b)
    return gcd(b,a%b)

if(__name__=='__main__'):
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    print(gcd(a,b))
