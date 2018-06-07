"""Partition a linked list around a value."""


from linked_list import Node, LinkedList


def partition_linkedlist(linklist, x):
    
    head = linklist.head

    if head is None or head.next is None:
        return linklist
    
    # find tail
    current = head
    while current.next is not None:
        current = current.next
    
    tail = current

    previous = None
    current = head
    new_tail = tail
    
    while current != tail:
        if current.value >= x:
            if current != head:
                previous.next = current.next
                new_tail.next = current
                current.next = None
                new_tail = current
                current = previous.next
            else:
                head = current.next
                new_tail.next = current
                current.next = None
                new_tail = current
                current = head
                
        else:
            previous = current
            current = current.next

    linklist.head = head
    return linklist


# # create a linked list
# a = [5, 6, 7]
# x = 5

# my_list = LinkedList()

# for item in a:
#     n = Node(item)
#     my_list.insert_at_tail(n)

# print(my_list.convert_to_list())

# # partition and print
# partition_linkedlist(my_list, x)
# print(my_list.convert_to_list())
