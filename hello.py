# UnboundLocalError

def a():
    x = 4
    def b():
        nonlocal x
        x += 1
        print(x)
    b()
a()
