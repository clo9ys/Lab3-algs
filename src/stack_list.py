class StackOnList:
    """
    Стек на списке.
    Поддерживает функции push/pop/peek/min/is_empty/print/len.
    """

    def __init__(self):
        self.lst = [] # наш стек

    def push(self, x: int) -> None:
        """
        Добавляет элемент x.
        """
        self.lst.append(x)

    def pop(self) -> int:
        """
        Извлекает верхний элемент стека.
        Выбрасывает IndexError если пусто.
        """
        if not self.lst:
            raise IndexError("pop from empty stack")
        return self.lst.pop()

    def is_empty(self) -> bool:
        """
        Проверяет пустоту стека.
        """
        return len(self.lst) == 0

    def __len__(self) -> int:
        """
        Длина стека.
        """
        return len(self.lst)

    def peek(self) -> int:
        """
        Смотрит верхний элемент, без извлечения.
        """
        if not self.lst:
            raise IndexError("peek from empty stack")
        return self.lst[-1]

    def min(self) -> int:
        """
        Минимум в стеке.
        """
        if not self.lst:
            raise IndexError("empty stack")
        return min(self.lst)
