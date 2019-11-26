# Write a Program to Create a List of Tuples with the First Element as the Number and Second Element as the Square of the Number

my_list = [int(x) for x in input('\nEnter numbers sperated by space: ').split()]

print('your numbers list is: ',my_list)

tuple_square_list = [(x,x*x) for x in my_list]

print('tuple square list is: ',tuple_square_list)
