"""Remove duplicates from a linked-list."""

def remove_duplicates(first_head):

    second_head = None
    second_tail = None
    current = first_head

    while current is not None:
        if not is_member(second_head, current.data):
            temp = Node(current.data)
            if second_tail is None:
                second_tail = temp
                second_head = temp
            else:
                second_tail.next = temp
                second_tail = temp

        current = current.next

    return second_head


def is_member(list_head, data):

    result = False
    if list_head is not None:
        while (list_head.data != data) and (list_head.next is not None):
            list_head = list_head.next

        if list_head.data == data:
            result = True

    return result


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


