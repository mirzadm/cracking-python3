"""Queue implementation."""


class QueueNode:

    def __init__(self, data=None):
        self.data = data
        self.next_node = None


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, data):
        node = QueueNode(data)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next_node = node
            self.tail = node
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise KeyError('Queue is empty.')
        else:
            node = self.head
            self.head = self.head.next_node
            if self.head is None:
                self.tail = None
            self.count -= 1
            return node.data

    def is_empty(self):
        return self.head is None        

    def size(self):
        return self.count
