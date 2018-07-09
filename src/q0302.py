"""Chapter 3: Question 2.

Implement a stack with an O(1) min() method.
"""

from src.utils.stack import Stack


class StackWithMin(Stack):
    """Uses a secondary stack to keep track of minimum values."""

    def __init__(self):
        super().__init__()
        self.min_stack = Stack()

    def push(self, item):
        if self.is_empty():
            self.min_stack.push(item) 
        elif item <= self.min():
            self.min_stack.push(item)
        super().push(item)

    def pop(self):
        item = super().peek() # Throws an exception if empty
        if self.min() == item:
            self.min_stack.pop()
        return super().pop()

    def min(self):
        if self.is_empty():
            raise IndexError('Stack is empty.')
        else:
            return self.min_stack.peek()
