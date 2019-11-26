# Write a program to Sort a List According to the Length of the Elements

names = [str(x) for x in input('Enter list of names sperated by comma: ').split(',')]

print('you have entered: ',names)

print(names.sort(key=len))

print('after sorting by size of each element:',names)
