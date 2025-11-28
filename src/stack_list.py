class StackOnList:
    def __init__(self):
        self.lst = []

    def push(self, x: int) -> None:
        self.lst.append(x)

    def pop(self) -> int:
        if not self.lst:
            raise IndexError("pop from empty stack")
        return self.lst.pop()

    def is_empty(self) -> bool:
        return len(self.lst) == 0

    def __len__(self) -> int:
        return len(self.lst)

    def peek(self) -> int:
        if not self.lst:
            raise IndexError("peek from empty stack")
        return self.lst[-1]

    def min(self) -> int:
        if not self.lst:
            raise IndexError("empty stack")
        return min(self.lst)