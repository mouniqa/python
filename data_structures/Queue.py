class Queue:

    def __init__(self):
        self.items = []
        self.length = 0
    def is_empty(self):
        return self.items == []
    def enqueue(self,item):
        self.length += 1
        self.items.insert(0,item)
    def dequeue(self):
        self.length -= 1
        return self.items.pop()
    def size(self):
        return length
    def get_items(self):
        return self.items

q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.dequeue()



print(q.length)

print()
print(q.get_items())
