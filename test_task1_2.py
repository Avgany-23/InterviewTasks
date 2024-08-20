from task1 import Stack
from task2 import check_balanced_brackets
import pytest


@pytest.fixture(scope='function')
def stack():
    stack = Stack()
    stack.push(1), stack.push(2)
    return stack


def test_pop_stack(stack):
    assert stack.pop() == 2, 'Удаляемый элемент должен быть равен 2'
    assert stack.pop() == 1, 'Удаляемый элемент должен быть равен 1'
    assert stack.is_empty(), 'Стек должен быть пустой'


@pytest.mark.parametrize('obj', [
    '123120',
    123,
    True,
    None,
    [1, {1, 2}],
    {'one': 1, 'two': 2},
])
def test_push(stack, obj):
    stack.push(obj)
    assert stack.peek() == obj, 'Добавляемый элемент стека должен быть равен %s' % obj


def test_count_after_push(stack):
    for obj in [
        ('123120', 3),
        (123, 4),
        (True, 5),
        (None, 6),
        ([1, {1, 2}], 7),
        ({'one': 1, 'two': 2}, 8),
    ]:
        stack.push(obj[0])
        assert stack.size() == obj[1], 'Размер стека должен быть равен %s' % obj[1]


@pytest.mark.parametrize('bracket', [
    ('(((([{}]))))', True),
    ('[([])((([[[]]])))]{()}', True),
    ('{{[()]}}', True),
    ('}{}', False),
    ('{{[(])]}}', False),
    ('[[{())}]', False),
])
def test_function_check_balanced_brackets(bracket):
    assert check_balanced_brackets(bracket[0]) == bracket[1], (f'Результат функции check_balanced_brackets с параметром'
                                                               f'{bracket[0]} должен быть {bracket[1]}')