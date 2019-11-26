d={
  1:'a',
  2:'b',
  3:'c',
  4:'d'
}

print(d)

key = eval(input('Enter the key to remove: '))

if key in d.keys():
  x=d[key]
  del d[key]
  print('key-{} and value-{} removed'.format(key,x))
  del x

else:
  print('key-{} does not exist'.format(key))

print(d)
