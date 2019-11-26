my_list_1 = [x for x in input('Enter number seperated by space: ').split()]
my_list_2 = [x for x in input('Enter numbers seperated by space: ').split()]

print('first list is: ',my_list_1)
print('second list is: ',my_list_2)

# Solution 1: Using plus + operator with sort()
new_list = my_list_1+my_list_2
new_list.sort()
print('new sorted list after merge: ',new_list)

# Solution 2: Using append() and sort()

new_list_2 = my_list_1[:]
for i in my_list_2:
    new_list_2.append(i)
new_list_2.sort()
print('new sorted list after append: ',new_list_2)

# Solution 3: Using extend() and sort()

new_list_3 = my_list_1[:]
new_list_3.extend(my_list_2)
new_list_3.sort()
print('new sorted list after extend: ',new_list_)
