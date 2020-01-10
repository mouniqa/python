class MaxStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self._items = []
        self._max_items = []
    def push(self, x: int) -> None:
        self._items.append(x)
        if len(self._max_items)==0:
            self._max_items.append(x)
        else:
            if x>=self._max_items[-1]:
                self._max_items.append(x)
    def pop(self) -> None:
        if len(self._items)>0:
            if self._items[-1]==self._max_items[-1]:
                self._max_items.pop()
        return self._items.pop()
    def top(self) -> int:
        if len(self._items)>0:
            return self._items[-1]
    def getMax(self) -> int:
        if len(self._items)>0:
            return self._max_items[-1]
