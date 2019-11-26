# Write a Program to Put Even and Odd elements in a List into Two Different Lists

my_list = [eval(x) for x in input('Enter list of numbers seperated by space: ').split()]

# Solution 1: Using list comprehention
print('\n# Solution 1: Using list comprehension')

print('original list is: ',my_list)

even_list = [x for x in my_list if x%2==0]
print('even list is: ',even_list)

odd_list = [x for x in my_list if x%2!=0]
print('odd list is: ',odd_list)

# Solution 2: Using append() function
print('\n# Solution 2: Using append() function')

print('original list is: ',my_list)

even_list = []
odd_list = []

for number in my_list:
    if number%2==0:
        even_list.append(number)
    else:
        odd_list.append(number)

print('even list is: ',even_list)
print('odd list is: ',odd_list)
