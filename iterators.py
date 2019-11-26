class Squares:
    def __init__(self,number):
        self.result = 0
        self.number = number
    def __iter__(self):
        self.result = 0
        return self
    def __next__(self):
        self.result += self.number
        return self.result

s = Squares(2)

while True:
    print(s.__next__())
    if next(s)>25:
        break
