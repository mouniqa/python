x = 'abcd'

print('Sub Sequences:')
print('-------------')
sub_seq = []
for i in range(len(x)):
    sub = x[i]
    if sub not in sub_seq:
        sub_seq.append(sub)
    for j in range(i+1,len(x)):
        sub = x[i]+x[j]
        if sub not in sub_seq:
            sub_seq.append(sub)
        for k in range(j+1,len(x)):
            sub += x[k]
            if sub not in sub_seq:
                sub_seq.append(sub)


print(len(sub_seq))
print(sub_seq)

print()

print('Sub Strings:')
print('-------------')

sub_strings = []
for i in range(len(x)):
    sub = x[i]
    sub_strings.append(sub)
    for j in range(i+1,len(x)):
        sub += x[j]
        sub_strings.append(sub)

print(len(sub_strings))
print(sub_strings)
