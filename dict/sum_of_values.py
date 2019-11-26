d = {int(x):int(x)*int(x) for x in input('Enter numbers seperated by space: ').split()}

print(d)

print('sum of the squares of the values you entered:\n{}'.format(sum(d.values())))
