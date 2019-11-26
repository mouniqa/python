n = [1,2,3,4,5]

for i in range(6):
    try:
        a = i+2
        print(n[a])
    except IndexError:
        print('Index out of bound error')
    else:
        print('In else block')
    finally:
        print('Entered in Finally block')
