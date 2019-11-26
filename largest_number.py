# Solution 1: Using max() function

my_list = eval(input('Enter the list of numbers: '))

print('\nSolution 1: Using max() function')
if type(my_list)==type(list()):
    print('max is: ',max(my_list))
else:
    print('TypeError: Expected {} but entered {}'.format(type(list()),type(my_list)))

# Solution 2: Using sort() function

print('\nSolution 2: Using sort() function')

if type(my_list)==type(list()):
    my_list.sort()
    print('max is: ',my_list[len(my_list)-1])
else:
    print('TypeError: Expected {} but entered {}'.fortmat(type(list()),type(my_list)))

# Solution 3: With out using any function

#TODO
