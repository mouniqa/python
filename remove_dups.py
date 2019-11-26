S = input('Enter any String: ')
no_dups = ''
for i in S:
    if i not in no_dups:
        no_dups += i
print(no_dups)
