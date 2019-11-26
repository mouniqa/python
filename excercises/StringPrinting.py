# Take integer N as input in first line
# Next take N strings as input in each line
# Print even indexed characters of the string and space then odd indexed characters.

N = int(input('Enter number: '))
S = [x for x input().split()]
for i in S:
    print(i[::2],i[1::2])
