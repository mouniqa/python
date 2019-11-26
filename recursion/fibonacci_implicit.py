from functools import lru_cache

@lru_cache(maxsize = 1000)
def fibonacci(n):
    if n>2:
        return fibonacci(n-1)+fibonacci(n-2)
    else:
        return 1

if (__name__ == '__main__'):

    n = int(input('Enter positive integer: '))

    for i in range(1,n+1):
        print(n,":",fibonacci(n))
