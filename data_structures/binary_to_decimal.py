from Stack import Stack
def bin_to_dec(number):
    s = Stack()
    while number>0:
        remainder = number%2
        s.push(remainder)
        number = number//2
    decimal =''
    while not s.is_empty():
        decimal += str(s.pop())
    return decimal

if __name__ == '__main__':
    number = int(input('Enter number: '))
    print(bin_to_dec(number))
