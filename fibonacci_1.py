# print nth fibonacci
n = int(input('Enter n: '))
a=0
b=1

def fib(n):
    if n < 0:
        print("Invalid input")
    if n == 1:
        print(1,end=', ')
        return 0
    if n == 2:
        print(2,end=', ')
        return 1
    if n > 1:
        print(n)
        return fib(n-1)+fib(n-2)

print()
print(fib(n))
