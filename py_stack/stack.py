class Stack:
    def __init__(self, init: list[str]) -> None:
        self.stack = init

    def push(self, value: str) -> None:
        if value == "" or value == None:
            return

        self.stack.append(value)

    def pop(self) -> str | None:
        if len(self.stack) == 0:
            return None

        return self.stack.pop()

    def peek(self) -> str | None:
        if len(self.stack) == 0:
            return None
        
        return self.stack[len(self.stack)-1]
