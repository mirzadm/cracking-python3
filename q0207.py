"""Check if a linked list is a palindrome."""


from linked_list import Node, LinkedList


def is_palindrome(link):
    
    if link is None or link.head is None:
        return False
    
    # find length
    cur = link.head
    k = 0
    while cur is not None:      
        cur = cur.next
        k += 1

    h = k // 2
    cur = link.head
    rev_link = LinkedList()

    while h != 0:
        n = Node(cur.value)
        n.next = rev_link.head
        rev_link.head = n
        cur = cur.next
        h -= 1

    if k % 2 == 1:
        cur = cur.next
    
    p = rev_link.head
    while p is not None:
        if p.value != cur.value:
            return False
        p = p.next
        cur = cur.next
    
    return True


# Using slow and fast pointers. 
# Time: O(n). Space: O(n)

def is_palindrome_slow_fast(link):

    if link is None or link.head is None:
        return None

    slow = fast = link.head

    if slow.next is None:
        return True
    elif slow.next.next is None:
        return slow.value == slow.next.value

    stack = []
    while fast.next is not None and fast.next.next is not None:
        stack.append(slow)
        fast = fast.next.next
        slow = slow.next
    
    # If odd number nodes in the list, pop the mid element
    if fast.next is not None:
        stack.append(slow)
    
    slow = slow.next
    
    while slow is not None:
        n = stack.pop()
        if n.value != slow.value:
            return False
        slow = slow.next
    
    return True


# a = [1, 2, 3, 2, 1]
# link = LinkedList()
# for item in a:
#     n = Node(item)
#     link.insert_at_head(n)

# print(is_palindrome_slow_fast(link))
