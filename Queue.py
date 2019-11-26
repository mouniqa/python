'''
Queue : FIFO

enqueue() - add element in a queue
dequeque() - remove the first added element
peek() - return the front element
isempty() - return boolean value (if the queue is empty or not)
isfull() - return boolean value (if the queue is empty or not)
'''
from collections import deque

class Queue:
    def __init__(self,maxlen=None):
        self._queue = deque([])
        self.count = 0
        self.maxlen = maxlen
    def add(self,value):
        if self.count>=self.maxlen:
            print('Queue is full. Can not add more elements')
        else:
            self._queue.append(value)
            self.count += 1
    def size(self):
        return self.count
    def remove(self):
        self.count -= 1
        return self._queue.popleft()
    def peek(self):
        return self._queue[0]
    def isempty(self):
        return not len(self._queue)
    def isfull(self):
        if self.maxlen == None:
            print('This queue can not be full as maxlen is not specified')
            return False
        elif self.count == self.maxlen:
            return True
        else:
            return False


if __name__ == '__main__':

    def display(obj):
        print()
        print('Front element -',obj.peek())
        print('Size -',obj.size())
        print('Is empty -',obj.isempty())
        print('Is full -',obj.isfull())

    q1 = Queue(4)
    q1.add('Jagadeesh')
    display(q1)
    q1.add('Mounika')
    q1.add('Varma')
    display(q1)
    print(q1.remove())
    display(q1)
    q1.add('Keetha')
    q1.add('Mouni')
    q1.add('Yo')
    q1.add('te')
    display(q1)
