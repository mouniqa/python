#Reverse the number
#This is my change - jagadeesh varma

rNum=int(input('Enter a number to be reversed : '))
res=0
while(rNum!=0):
    temp=rNum%10
    res=res*10+temp
    rNum=int(rNum/10)

print("Number got reversed :",res)
