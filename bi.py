# 2 4 5 7 8 9 11 14 23 27 34 36 48 59 67 71 84 92
# 0 1 2 3 4 5  6  7  8  9 10 11 12 13 14 15 16 17

def binary_search(sequence,key):
  low = 0
  high = len(sequence) - 1

  while(len(sequence)>1):
    mid = int((low+high)/2)
    print(sequence[low:high+1],' -->',sequence[mid])
    if key < sequence[mid]:
      high = mid - 1
    elif key > sequence[mid]:
      low = mid + 1
    else:
      return mid

if(__name__=='__main__'):
  s = '2 4 5 7 8 9 11  1423  27  34  36  48  59  67  71  84  92'
  sequence = [int(x) for x in input('Enter sequence: ').split()]
  key = int(input('Enter key: '))
  print(binary_search(sequence,key))
