print('\n**************************************************')
print('*  This program gives you the result of below    *')
print('*  math operations performed on given input a,b   *')
print('*    → Addition ( + )                            * ')
print('*    → Mulitplication ( * )                      *')
print('*    → Substraction ( -  )                       *')
print('*    → Division ( / )                            *')
print('*    → Mod ( % )                                 *')
print('*    → Power ( ** )                              *')
print('*    → Quotient ( // )                           *')
print('**************************************************\n')


class Calc:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
      return self.a+self.b
    def sub(self):
      return self.a-self.b
    def mult(self):
      return self.a*-self.b
    def div(self):
      return self.a/self.b
    def mod(self):
      return self.a%self.b
    def pow(self):
      return self.a**self.b
    def true_div(self):
      return self.a//self.b

a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = Calc(a,b)

choice = 1
while choice != 0:
  print('Enter any below operation to perform.\n  +  -  *  /  %  **  //  : ',end='')
  op = input()
  if op == '+':
    print(c.add())
  elif op == '-':
    print(c.sub())
  elif op == '*':
    print(c.mult())
  elif op == '/':
    try:
      print(c.div())
    except ZeroDivisionError:
      print('ERROR: Can\'t be devided by zero.')
  elif op == '%':
    print(c.mod())
  elif op == '**':
    print(c.pow())
  elif op == '//':
    print(c.true_div())
  else:
    print('Invalid Operation')
  print('\n=====================================\n')
  print('Hit Enter to continue')
  print('Type 0 [zero] and hit enter to exit')
  try:
    choice=eval(input())
  except:
    continue
