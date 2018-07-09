"""Stack implementation."""


class Stack:
    """Simple stack implementation using list."""

    def __init__(self):
        self.stack_list = []

    def push(self, item):
        self.stack_list.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is empty.')
        else:
            return self.stack_list.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError('Stack is empty.')
        else:
            return self.stack_list[-1]

    def is_empty(self):
        return self.stack_list == []

    def size(self):
        return len(self.stack_list)