# Palindrom:
# a word, phrase, or sequence that reads the same backwards as forwards,
# e.g. madam or nurses run.
#
# In this excercise we only check numbers.
# e.g. n = 1221 is palindrom
#      n = 1234 is not palindrom

rNum=int(input('Enter a number to be reversed : '))
result=0
storerNum=rNum
while(rNum!=0):
    digit=rNum%10
    result=result*10+digit
    rNum=int(rNum/10)

print("Number got reversed :",result)

if(storerNum == result):
    print("Gven number is  a  Palindrom")
else:
    print("Given is not a Palindrom")
