from typing import Any


class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return not bool(self.stack)

    def push(self, obj: Any):
        self.stack.append(obj)

    def pop(self):
        return self.stack.pop() if self.stack else None

    def peek(self):
        return self.stack[-1] if self.stack else None

    def size(self):
        return len(self.stack)