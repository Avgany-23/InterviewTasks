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


brackets = ['(((([{}]))))', '[([])((([[[]]])))]{()}', '{{[()]}}', '}{}', '{{[(])]}}', '[[{())}]']


def check_balanced_brackets(brackets):
    dict_brackets = {']': '[',
                     ')': '(',
                     '}': '{'}
    stack = Stack()
    count = -1
    count_brackets = len(brackets)
    while (count := count + 1) < count_brackets:
        add_element = brackets[count]
        if add_element in dict_brackets:
            if stack.pop() != dict_brackets[add_element]:
                return False
            continue
        stack.push(add_element)
    return stack.is_empty()