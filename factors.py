def prime_factors(n):
  prime_factors= []
  i=2
  while(n>1):
    if n%i==0:
      n = n//i
      prime_factors.append(i)
      i = 2
    else:
      i+=1
  return prime_factors

if __name__ == '__main__':
    n = int(input('Enter any Integer: '))
    print(prime_factors(n))
