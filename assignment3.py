#Reverse the number
#This is my change - jagadeesh varma

rNum=int(input('Enter a number to be reversed'))
#comment by suman
while(rNum!=0):
    res=rNum%10
    rNum=rNum/10
    print(res)
