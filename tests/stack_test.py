import pytest
from py_stack.stack import Stack  

def test_stack_initialization():
    init_values = [1, 2, 3]
    stack = Stack(init_values)
    assert stack.stack == init_values

def test_push():
    stack = Stack([])
    stack.push(4)
    assert stack.stack == [4]

    stack.push(5.5)
    assert stack.stack == [4, 5.5]

    stack.push("hello")
    assert stack.stack == [4, 5.5, "hello"]

def test_push_empty_value():
    stack = Stack([1, 2, 3])
    stack.push(None)
    assert stack.stack == [1, 2, 3]

def test_pop():
    stack = Stack([4, 5, 6])
    popped_value = stack.pop()
    assert popped_value == 6
    assert stack.stack == [4, 5]

def test_pop_empty_stack():
    stack = Stack([])
    popped_value = stack.pop()
    assert popped_value is None
    assert stack.stack == []

def test_peek():
    stack = Stack([7, 8, 9])
    top_value = stack.peek()
    assert top_value == 9
    assert stack.stack == [7, 8, 9]

def test_peek_empty_stack():
    stack = Stack([])
    top_value = stack.peek()
    assert top_value is None
    assert stack.stack == []

def test_push_mixed_types():
    stack = Stack([])
    stack.push(1)
    assert stack.stack == [1]

    stack.push("abc")
    assert stack.stack == [1, "abc"]

    stack.push(3.14)
    assert stack.stack == [1, "abc", 3.14]

def test_pop_mixed_types():
    stack = Stack(["xyz", 42, True])
    popped_value = stack.pop()
    assert popped_value is True
    assert stack.stack == ["xyz", 42]

if __name__ == "__main__":
    pytest.main(['stack_test.py'])

