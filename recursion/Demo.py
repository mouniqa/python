def demo(n=1)->int:
    print(n)
    if n>=10:
        return 1
    demo(n+1)
demo()
