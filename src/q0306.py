"""Chapter 3: Question 6.

Sort a stack using one additional stack and not other data structure.
"""

from src.utils.stack import Stack


def sort_stack_iterative(s1):
    """Sorts s1 interatively using a scondary stack. 

    Ascending sort: bigger items on top.
    """

    s2 = Stack()
    # Sort items in descending order in s2
    while not s1.is_empty():
        next_item = s1.pop()
        count = 0
        while not s2.is_empty() and next_item > s2.peek():
            s1.push(s2.pop())
            count += 1

        s2.push(next_item)
    
        while count > 0:
            s2.push(s1.pop())
            count -= 1
    # Move items back to s1 and reverse the order to ascedning
    while not s2.is_empty():
        s1.push(s2.pop())


def sort_stack_recursive(n, s1, s2):
    """Sorts top n items in s1 recursively using s2.

    Ascending sort: bigger items on top.
    """
    if n >= 2:
        sort_stack_recursive(n-1, s1, s2)

        count = n - 1
        while count > 0:
            s2.push(s1.pop())
            count -= 1

        next_item = s1.pop()
        while not s2.is_empty() and next_item > s2.peek():
            s1.push(s2.pop())
        s1.push(next_item)
        while not s2.is_empty():
            s1.push(s2.pop())
