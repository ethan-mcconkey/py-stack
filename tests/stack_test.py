import pytest
from py_stack.stack import Stack

def test_stack_initialization():
    init_values = ["a", "b", "c"]
    stack = Stack(init_values)
    assert stack.stack == init_values

def test_push():
    stack = Stack([])
    stack.push("a")
    assert stack.stack == ["a"]

    stack.push("b")
    assert stack.stack == ["a", "b"]

def test_push_empty_value():
    stack = Stack(["a", "b"])
    stack.push("")
    assert stack.stack == ["a", "b"]

def test_push_none_value():
    stack = Stack(["a", "b"])
    stack.push("")
    assert stack.stack == ["a", "b"]

def test_pop():
    stack = Stack(["a", "b", "c"])
    popped_value = stack.pop()
    assert popped_value == "c"
    assert stack.stack == ["a", "b"]

def test_pop_empty_stack():
    stack = Stack([])
    popped_value = stack.pop()
    assert popped_value is None
    assert stack.stack == []

def test_peek():
    stack = Stack(["x", "y", "z"])
    top_value = stack.peek()
    assert top_value == "z"
    assert stack.stack == ["x", "y", "z"]

def test_peek_empty_stack():
    stack = Stack([])
    top_value = stack.peek()
    assert top_value is None
    assert stack.stack == []

# Add more test cases as needed

if __name__ == "__main__":
    pytest.main()

