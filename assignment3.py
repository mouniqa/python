#Reverse the number

rNum=int(input('Enter a number to be reversed'))

while(rNum!=0):
    res=rNum%10
    rNum=rNum/10
    print(res)
    
