class MyQueue:
    def __init__(self):
        self.push_stack = []
        self.pop_stack = []

    def push(self, x: int) -> None:
        self.push_stack.append(x)

    def shift_stacks(self) -> None:
        if not self.pop_stack:
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())

    def pop(self) -> int:
        self.shift_stacks()
        return self.pop_stack.pop()

    def peek(self) -> int:
        self.shift_stacks()
        return self.pop_stack[-1]

    def empty(self) -> bool:
        return not self.push_stack and not self.pop_stack

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()