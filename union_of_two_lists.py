list_one = [x for x in input('Enter the list seperated by comma:').split(',')]
list_two = [x for x in input('Enter the list seperated by comma:').split(',')]

def get_union(list1,list2):
    union = []
    for i in list_one:
        union.append(i)
    for j in list_two:
        if j not in union:
            union.append(j)
    return union

print('list one is: ',list_one)
print('list two is: ',list_two)
print('union of two lists is: ',get_union(list_one,list_two))
