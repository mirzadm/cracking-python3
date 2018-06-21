"""Find kth last element in a singly linked list."""


def kth_last(head, k):
    if head is None or k < 1:
        return None

    tail = head
    kth = None
    
    # move tail k-1 steps forward
    for _ in range(k-1):
        if tail.next is None:
            return None
        else:
            tail = tail.next
    
    kth = head

    while tail.next is not None:
        tail = tail.next
        kth = kth.next
    
    return kth.value


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
for i in range(1, 11):
    n = Node(i)
    a.insert_at_head(n)

print(a.convert_to_list())
print(kth_last(a.head, 7))


