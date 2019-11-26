my_list = eval(input('Enter the list of numbers: '))

def second_max(list):
    m = max(list)
    while m in list:
        list.remove(m)
    return max(list)

print('second max is: ',second_max(my_list))
