d={}
update_dict = 'yes'
while(update_dict=='yes'):
    key = eval(input('Enter the key: '))
    value = eval((input('Enter the value: ')))
    update_dict=input('Do you want to continue[yes/no]: ')
    d.update({key:value})

print(d)
