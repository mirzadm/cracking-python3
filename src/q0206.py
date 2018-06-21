""""Find the loop is a corrupted linked list."""

from linked_list import Node, LinkedList

def find_loop(link):    
    if link is None or link.head is None:
        return None

    sofar = set()
    cur = link.head

    while cur is not None:
        if cur not in sofar:
            sofar.add(cur)
        else:
            return cur
        cur = cur.next

    return None


# ----------------------------------------------------------------------------
# Solution using fast and slow pointers: O(n) time, O(1) space

def find_loop_slow_fast(link):

    if link is None or link.head is None:
        return None
    
    # move slow and fast until they meet
    slow = link.head
    fast = link.head
    while True:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            break
    
    k = 0
    while True:
        fast = fast.next.next
        slow = slow.next
        k += 1
        if slow == fast:
            break

    p = link.head
    pk = link.head
    while k != 0:
        pk = pk.next
        k -= 1
    while p != pk:
        p = p.next
        pk = pk.next

    return p


# ----------------------------------------------------------------------------
# Solution using fast and slow pointers: O(n) time, O(1) space
# A simpler implementation
def find_loop_slow_fast2(link):

    if link is None or link.head is None:
        return None

    slow1 = link.head
    fast = link.head
    while True:
        slow1= slow1.next
        fast = fast.next.next
        if slow1 == fast:
            break
            
    slow2 = link.head
    while slow1 != slow2:
        slow1 = slow1.next
        slow2 = slow2.next
    
    return slow1


# # create a corrupted linked list
# link = LinkedList()
# n1 = Node(1)
# n2 = Node(2)
# n3 = Node(3)
# link.head = n1
# n1.next = n2
# n2.next = n3
# n3.next = n3

# print(find_loop_slow_fast2(link).value)
