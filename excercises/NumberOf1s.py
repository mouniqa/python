# Find the number of consequitive 1s after converting a decimal number to binary number.
# Take decimal number as input, Convert it into binary, count the number of consequitive 1s.

n = int(input())
# count = str(bin(decimal))[2:].split('0')
count = len(max(str(bin(n))[2:].split('0')))
print(count)
