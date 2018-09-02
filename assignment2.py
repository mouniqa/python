num1=int(input("Enter  number 1 : "))
num2=int(input("Enter  number 2 : "))
num3=int(input("Enter  number 3 : "))

if(num1>num2>num3):
    print(num1,"is the greatest of three numbers")
elif(num2>num3):
    print(num2,"is the greatest of three numbers")
else:
    print(num3,"is the greatest of the three numbers ")


# in first conditon(if) we are checking num1 so we can eliminate it in elif
# Also we can use num2<num1>num3 which is same as num1>num2 and num1>num3
