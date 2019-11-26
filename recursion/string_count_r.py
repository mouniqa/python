#How Many Times a Given Letter Occurs in a String Recursively

char,string = [x for x in input('\nEnter char and string seperated by comma: ').split(',')]

def find_ch(char,string):
    if not string:
        return 0
    elif char == string[0]:
        return 1+find_ch(char,string[1:])
    else:
        return find_ch(char,string[1:])

print('searching for "{}" in "{}"'.format(char,string))
print('found "{}" times'.format(find_ch(char,string)))
