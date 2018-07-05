"""Chapter 2: Question 5.


Add two numbers represented by linked lists and return the result as a linked
list.
1 -> 2 -> 3     321
4 -> 5           54
                375 
"""

from src.utils.linkedlist import LinkedList, Node


def add_linkedlist_nums(linked_list1, linked_list2):
    """Returns sum of two linked lists representing numbers.

    Args:
        linked_list1: First number. A LinkedList instance object.
        linked_list2: Second number. A LinkedList instance object.
    Returns:
        Sum as a LinkedList instance object. 
    """

    sum_linked_list = LinkedList()        
    current1 = linked_list1.head
    current2 = linked_list2.head
    current3 = None
    carry = 0
    while current1 or current2:
        subsum = carry
        if current1:
            subsum += current1.data
            current1 = current1.next_node
        if current2:
            subsum += current2.data
            current2 = current2.next_node

        carry = subsum // 10
        node = Node(subsum % 10)
        if not current3:
            sum_linked_list.head = node
            current3 = node
        else:
            current3.next_node = node
            current3 = node
    
    if carry == 1:
        node = Node(1)
        current3.next_node = node

    return sum_linked_list
