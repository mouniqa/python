#.1.1<=n<=1000000
#2.if n is odd print odd
# if n is even and 1<n<=100 --> Print ok
#.if n is even and 101<=n<==1000 print nice
#.if n is even and n>1000 print awesome

n=int(input("Enter your number : "))
if(n>=1 and n<=1000000):
    if(not(n%2==0)):
        print("Odd")
    elif(n%2==0 and n<=100):
        print("OK")
    elif(n%2==0 and n<=1000):
        print("Nice")
    elif(n>1000):
        print("Awesome")

else:
    print("Constraint Violated")
