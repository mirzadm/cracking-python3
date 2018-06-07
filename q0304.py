"""Towers of Hanoi."""


def hanoi_towers(n ,s1, s2, s3):
    if n == 1:
        s2.push(s1.pop())
        s3.push(s2.pop())
    else:   
        hanoi_towers(n-1, s1, s2, s3)
        s2.push(s1.pop())
        hanoi_towers(n-1, s3, s2, s1)
        s3.push(s2.pop())
        hanoi_towers(n-1, s1, s2, s3)


class Node:
    def __init__(self):
        self.value = None
        self.next = None


class Stack:
    
    def __init__(self):
        self.top = None

    def push(self, item):
        n = Node()
        n.value = item
        if self.is_empty():
            self.top = n
        else:
            n.next = self.top
            self.top = n

    def pop(self):
        if self.is_empty():
            return None
        else:
            t = self.top.value
            self.top = self.top.next
            return t
    
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.top.value

    def is_empty(self):
        return self.top is None 


def test():
    a = list(range(10, 0, -1))
    s1 = Stack()
    s2 = Stack()
    s3 = Stack()
    for i in a:
        s1.push(i)

    hanoi_towers(5, s1, s2, s3)
    print('Stack 1')
    while not s1.is_empty():
        print(s1.pop())
    
    print('Stack 2')
    while not s2.is_empty():
        print(s2.pop())

    print('Stack 3')
    while not s3.is_empty():
        print(s3.pop())


if __name__ == '__main__':
    test()

