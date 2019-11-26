def love(age,job):
    assert (age > 20),'You should wait until you cross 20'
    assert (job == 'yes'),'First get job'
    print('You are now allowed for another aspect of life')

if __name__ == '__main__':
    age,job = (eval(x) for x in input().split())
    print(age,job)
    love(age,job)
