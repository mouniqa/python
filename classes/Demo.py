class Demo:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def display(self):
    print('name is {}\nage is {}'.format(self.name,self.age))

d1 = Demo('Jagadeesh',22)
d2 = Demo('Mounika',25)


d1.test()
