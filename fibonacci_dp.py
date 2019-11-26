import time

print('Normal Solution')
def f(n):
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    return f(n-1)+f(n-2)

start = time.time()
for i in range(35):
    f(i)
end = time.time()
print()
time1 = end-start
print(end-start)

print('---------------------')
print('DP Solution:')
def fib(n):
    d = {0:0,1:1,2:1}
    for i in range(3,n+1):
        d[i] = d[i-1]+d[i-2]
    return d[n]


start = time.time()
for i in range(35):
    fib(i)
end = time.time()
time2 = end-start
print(end-start)
print()
print()
print(time1/time2)
