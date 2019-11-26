sentense = input('Enter any sentense: ')

words = sentense.split()

d = {}

for word in words:
    if word[0] not in d.keys():
        d[word[0]] = [word]
    else:
        if word not in d[word[0]]:
            d[word[0]].append(word)

print(d)
print()
for key,value in d.items():
    print(key,' - ',value)
