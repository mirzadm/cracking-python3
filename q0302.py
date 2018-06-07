"""A stack with O(1) min method."""


class Stack:
    
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.stack == []:
            return None
        else:
            return self.stack.pop()

    def peek(self):
        if self.stack == []:
            return None
        else:
            return self.stack[-1]


class StackWithMin(Stack):

    def __init__(self):
        super().__init__()
        self.min_stack = Stack()

    def push(self, item):
        super().push(item)
        min_value = self.min()
        if min_value is None:
            self.min_stack.push(item) 
        elif item <= self.min():
            self.min_stack.push(item)

    def pop(self):
        item = super().pop()
        if item is not None:
            if self.min() == item:
                self.min_stack.pop()

        return item

    def min(self):
        return self.min_stack.peek()


# s = StackWithMin()
# a = [1, 2, 3, 1, 0, 4]
# for i in a:
#     s.push(i)

# while s.peek() is not None:
#     print('min: {}  peek: {}'.format(s.min(), s.peek()))
#     s.pop()
