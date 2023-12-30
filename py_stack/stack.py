from typing import TypeVar


T = TypeVar("T")

class Stack[T]:
    def __init__(self, init: list[T] = []) -> None:
        self.stack = init

    def push(self, value: T) -> None:
        if value == "" or value == None:
            return

        self.stack.append(value)

    def pop(self) -> T | None:
        if len(self.stack) == 0:
            return None

        return self.stack.pop()

    def peek(self) -> T | None:
        if len(self.stack) == 0:
            return None
        
        return self.stack[len(self.stack)-1]
