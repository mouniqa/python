# take a number as input and print the sum of the digits as output
# e.g.,
#     1: n = 1234
#       result = 1+2+3+4 = 10
#     2: n=23
#       result = 5

sOfDigits=int(input("Enter number to be summed up of : "))

res=0

while(sOfDigits != 0):
    temp=sOfDigits%10
    res=res+temp
    sOfDigits=int(sOfDigits/10)
print("Summation of numbers is : ",res)
