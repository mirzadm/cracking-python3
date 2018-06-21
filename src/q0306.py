"""Sort a stack using one additional stack."""


def sort_stack(s1):
    s2 = Stack()
    while not s1.is_empty():
        t = s1.pop()
        c = 0
        while not s2.is_empty() and t > s2.peek():
            k = s2.pop()
            s1.push(k)
            c += 1

        s2.push(t)
    
        while c > 0:
            s2.push(s1.pop())
            c -= 1

    while not s2.is_empty():
        s1.push(s2.pop())

    return s1


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
    a = [7, 4, 3, 5, 2, 1, 6]
    s = Stack()
    for i in a:
        s.push(i)
    sort_stack(s)
    while not s.is_empty():
        print(s.pop())


if __name__ == '__main__':
    test()

