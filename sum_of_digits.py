# take a number as input and print the sum of the digits as output
# e.g.,
#     1: n = 1234
#       result = 1+2+3+4 = 10
#     2: n=23
#       result = 5

print('\nThis program will give you the sum of digits of any number that you enter.')
number=int(input("Enter any number: "))
copy_of_number = number

result=0

while(number != 0):
    digit=number%10
    result=result+digit
    number=int(number/10)
print('\nSum of the digits of {} is : {}\n'.format(copy_of_number,result))
