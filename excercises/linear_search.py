# Linear search algorithm here
def linear_search(values,key):
    numberExists = False
    for number in values:
        print('searching....')
        if number == key:
            print('Found',number,'in',values)
            numberExists = True
            break
    if(not(numberExists)):
        print(key,'Not Found')


# Excutable code here

if __name__=='__main__':
    sorted_numbers = [int(x) for x in input('Enter numbers seperated by space in ascending order: ').split()]
    search_number = int(input('Enter the number you want to search: '))
    linear_search(sorted_numbers,search_number)
