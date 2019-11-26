class A:
    def __init__(self,a,b):
        self.a=1
        self.b=2

a=A('name','age')
print(a.__dict__)
print(a.a)
print(a.b)
