def squares():
    '''Generates squares on demand'''
    i = 1
    while True:
        yield i*i
        i += 1

for num in squares():
    print(num)
    if num>=100:
        break
