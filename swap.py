# swap two variables in simple way

x,y = [n for n in input('Enter numbers seperated by space: ').split()]

print('x = {} and y = {}'.format(x,y))

x,y=y,x

print('after swapping')

print('x = {} and y = {}'.format(x,y))
