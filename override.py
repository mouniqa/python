#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3

numbers = [int(x)*int(x) for x in input('Enter numbers: ').split()]

print(numbers)

for number in numbers:
    print(number)
