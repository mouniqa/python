my_list = [eval(x) for x in input('\nEnter list of elements seperated by space:').split()]

print('your list: ',my_list)

last = len(my_list)-1

temp = my_list[0]

my_list[0]  = my_list[len(my_list)-1]

my_list[len(my_list)-1] = temp

print('your list: ',my_list)
