# Write a program to Sort a List of Tuples in Increasing Order by the Last Element in Each Tuple

tuple_list = [eval(x) for x in input('enter list of tuples seperated by space: ').split()]

print(tuple_list)

def sort_tuple_list(list):
    temp=0
    for tuple in list:
        if tuple[len(tuple)-1]
