from task1 import StackLIFO, StackFIFO, ObjList
from task2 import check_balanced_brackets
import pytest


@pytest.fixture(scope='function')
def stack():
    stack = StackLIFO()
    stack.push(1), stack.push(2)
    return stack


def test_pop_stack_lifo(stack):
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
def test_push_stack_lifo(stack, obj):
    stack.push(obj)
    assert stack.peek() == obj, 'Добавляемый элемент стека должен быть равен %s' % obj


def test_count_after_push_stack_lifo(stack):
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


@pytest.mark.parametrize('obj', [3, 4, 5, 6, 7, 8, 9, 10])
def test_push_stack_fifo(obj):
    fifo = StackFIFO()
    for i in range(obj):
        fifo.push(ObjList(i))
        assert fifo.head.obj == 0, 'Головной элемент должен быть равен 0, а не %s' % fifo.head
        assert fifo.tail.obj == i, 'Хвостовой элемент должен быть равен на %s'
    assert fifo.len_stack == obj, 'Длина стека должна быть = %s' % obj
    fifo.pop(), fifo.pop()
    assert fifo.len_stack == obj - 2, 'Длина стека должна быть = %s' % (obj - 2)
    for _ in range(10):
        fifo.pop()
    assert fifo.len_stack == 0, 'Длина стека должна быть равна нулю'
    assert fifo.head is None, 'Головной элемент должен ссылаться на None'
    assert fifo.tail is None, 'Хвостовой элемент должен ссылаться на None'
