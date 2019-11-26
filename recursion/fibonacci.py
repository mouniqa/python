# Print the nth fibonachi number

fibonacci_cache = {}

def fibonacci(n):

    if n in fibonacci_cache:
        return fibonacci_cache[n]

    if n>2:
        value = fibonacci(n-1)+fibonacci(n-2)
    else:
        return 1

    fibonacci_cache[n] = value
    return value

if(__name__ == '__main__'):
    n = int(input('Enter a positive integer: '))

    for i in range(1,n+1):
        print(i,':',fibonacci(i))
