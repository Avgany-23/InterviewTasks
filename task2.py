from task1 import StackLIFO


def check_balanced_brackets(brackets: str) -> bool:
    dict_brackets = {']': '[',
                     ')': '(',
                     '}': '{'}
    stack = StackLIFO()
    count = -1
    count_brackets = len(brackets)
    while (count := count + 1) < count_brackets:
        add_element = brackets[count]
        if add_element in dict_brackets:
            if stack.pop() != dict_brackets[add_element]:
                return False
            continue
        stack.push(add_element)
    return True  # Или return stack.is_empty()