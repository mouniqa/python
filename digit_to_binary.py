number = int(input('Enter any number: '))

binaries = []

while(number>0):
    binaries.append(number%2)
    number = number//2

for i in binaries:
    print(i,end=" ")
print()
