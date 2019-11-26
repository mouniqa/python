# Binary search algorithm here

def binary_serach(key,values):
    print('searching...')
    index = int(len(values)/2)
    if(key<values[index]):
        values = values[:index]
    elif(key>values[index]):
        values = values[index:]
    elif(key==values[index]):
        print('Found',key)
        return 0
    else:
        print(key,'Not Found')
        return 0
    binary_serach(key,values)

def bisearch(key,values):
    index = int(len(values)/2)
    if(key<values[index]):
        valuesvalues[:index]
    elif(key>values[index]):
        bisearch(key,values[index+1:])
    else:
        return index
    print(key,'Not Found')
    return False

# Excutable code for this file is here

if __name__ == '__main__':

    numbers = [int(x) for x in range(1000)]
    n = int(input('Enter number to search: '))
    binary_serach(n,numbers)
    print(bisearch(n,numbers))
