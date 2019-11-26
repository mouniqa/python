print('\nThis program takes a list as input and removes duplicates from it.\n')

my_list = [eval(x) for x in input('Enter any list spereated by space: ').split()]
print('\nYour list is: ',my_list)

#Note: This method works in O(n^2) time and is thus very slow on large lists.
def remove_dup(dup_list):
    dup_list = []
    for i in my_list:
        if i not in dup_list:
            dup_list.append(i)
    return dup_list

# Another tricky method
tricky = []
test =  [tricky.append(i) for i in my_list if i not in tricky]

print('tricky: ',tricky)
# Simple solution using set() ↓ if order is not importanta
# dup_list = set(my_list)
# my_list = list(dup_list)

print('\nAfter removing duplicates: ',remove_dup(my_list))
