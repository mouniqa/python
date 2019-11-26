S = 'jagadeesh'
d = {}
for i in range(len(S)):
    if S[i] in d.keys():
        d[S[i]] += 1
    else:
        d[S[i]] = 1
print(d)

for i in range(len(S)):
    if d[S[i]] == 1:
        print(S[i])
        break
