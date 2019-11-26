# Python Program to Read a List of names and Return the the Longest One

names = [str(x) for x in input('Enter name seperated by comma: ').split(',')]
print(names)

def max_length(list):
    l=[]
    for name in names:
        l.append(len(name))
    return max(l)

def longest_name(list):
    longest=names[0]
    for n in list:
        if len(n)>len(longest):
            longest=n
    return longest



print('Length of the longest one: ',max_length(names))
print('Longest name is: ',longest_name(names))
