class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self._items = []
        self._min_items = []
    def push(self, x: int) -> None:
        self._items.append(x)
        if len(self._min_items)==0:
            self._min_items.append(x)
        else:
            if x<=self._min_items[-1]:
                self._min_items.append(x)
    def pop(self) -> None:
        if len(self._items):
            if self._items[-1]==self._min_items[-1]:
                self._min_items.pop()
            return self._items.pop()

    def top(self) -> int:
        if len(self._items)>0:
            return self._items[-1]

    def getMin(self) -> int:
        if len(self._min_items)>0:
            return self._min_items[-1]



s = MinStack()
s.push(0)
s.push(1)
s.push(0)

s.getMin()
s.pop()
s.getMin()
