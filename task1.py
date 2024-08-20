from typing import Any, Optional


class StackLIFO:
    def __init__(self) -> None:
        self.stack = []

    def is_empty(self) -> bool:
        """Проверка на пустоту стека"""
        return not bool(self.stack)

    def push(self, obj: Any) -> None:
        """Добавляет элемент в конец стека"""
        self.stack.append(obj)

    def pop(self) -> Optional[Any]:
        """Удаляет элемент с конца стека и возвращает его"""
        return self.stack.pop() if self.stack else None

    def peek(self) -> Optional[Any]:
        """Возвращает последний элемент стека"""
        return self.stack[-1] if self.stack else None

    def size(self) -> int:
        """Возвращает размер стека"""
        return len(self.stack)

# ---------------------------------------------------------------------------


class ObjList:
    def __init__(self, obj):
        self.obj = obj
        self.next = None

    def __str__(self):
        return str(self.obj)

    def __repr__(self):
        return self.obj


class StackFIFO:
    def __init__(self):
        self.head = None    # Первый элемент стека
        self.tail = None    # Последний элемент стека
        self.len_stack = 0

    def is_empty(self) -> bool:
        """Проверка на пустоту стека"""
        return self.head is None

    def push(self, obj: Any) -> None:
        """Добавляет элемент в конец стека"""
        if self.head is None:
            self.head = self.tail = obj
        else:
            self.tail.next = obj
            self.tail = obj
        self.len_stack += 1

    def pop(self) -> Optional[Any]:
        """Удаляет элемент с начала стека и возвращает его"""
        delete_obj = self.head
        if self.head == self.tail:
            self.head = self.tail = None
            self.len_stack = 0
        else:
            self.head = self.head.next
            self.len_stack -= 1
        return delete_obj

    def peek(self) -> Optional[Any]:
        """Возвращает последний элемент стека"""
        return self.tail

    def size(self) -> int:
        """Возвращает размер стека"""
        return self.len_stack