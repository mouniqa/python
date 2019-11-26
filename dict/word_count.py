sentense = input('Enter a sentense: ')
sentense_list = sentense.split()

dict = {string:sentense_list.count(string) for string in sentense_list}

print(dict)
