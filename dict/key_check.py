my_dict = {
  'one':1,
  'two':2,
  'three':3,
  1:'a',
  2:'b'
}

#print(my_dict)
#print(my_dict['one'])
#print(my_dict[1])
#print(my_dict['three'])
#print(my_dict.get(3))

key = eval(input('Enter the key you want to check: '))

print(my_dict.keys())

if key in my_dict.keys():
  print("key exists")
  print('{} : {}'.format(key,my_dict[key]))
else:
  print('key does not exist')
