"""Delete an element in the middle of a linked list."""


def del_mid_element(node):
    # it can't be the last node
    if node.next is None:
        return

    current = node
    while current.next is not None:
        previous = current
        current = current.next
        previous.value = current.value

    previous.next = None        
    del current


# ----------------------------------------------------------------------------
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
    
    def insert_at_head(self, node):
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
    
    def insert_at_tail(self, node):
        if self.head is None:
            self.head = node
        else:
            p = self.head
            while p.next is not None:
                p = p.next
            p.next = node

    def convert_to_list(self):
        p = self.head
        array = []
        while p is not None:
            array.append(p.value)
            p = p.next

        return array


# ----------------------------------------------------------------------------
a = LinkedList()
for i in range(5):
    n = Node(i)
    a.insert_at_head(n)

print(a.convert_to_list())
del_mid_element(a.head.next.next)
print(a.convert_to_list())


