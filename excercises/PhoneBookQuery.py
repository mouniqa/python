# Create a phone of dict type from user input e.g., phonebook={name1:number1,name2:number2,....}
# Take search strings(names) as input and return the contatc details in the format of name1 = number1
# In case the name is not in the phonebook print name1 = Not Found


n = int(input())

if(1<=n<=100000):

    dict = {(x for x in input().split()) for y in range(n)}

    phonebook = {x:y for (x,y) in dict}

    names = [input() for x in range(n)]

    for name in names:
        if(phonebook.get(name)!=None):
            print(name,'=',phonebook.get(name))
        else:
            print(name,'= Not Found')
