"""Add two linked lists representing two numbers."""


from linked_list import Node, LinkedList


def add_linkedlists_back(link1, link2):
    
    result = LinkedList()
    if link1.head is None and link2.head is None:
        return result

    cur1 = link1.head
    cur2 = link2.head
    cur3 = None
    carry = 0

    while cur1 is not None or cur2 is not None:
        subsum = carry
        if cur1 is not None:
            subsum += cur1.value
            cur1 = cur1.next
        if cur2 is not None:
            subsum += cur2.value
            cur2 = cur2.next

        carry = subsum // 10
        n = Node(0)
        n.value = subsum % 10
        if cur3 is None:
            result.head = n
            cur3 = n
        else:
            cur3.next = n
            cur3 = n
    
    if carry == 1:
        n = Node(1)
        cur3.next = n
        
    
    return result


# ----------------------------------------------------------------------------
# Followup: what if number are given in forward order


def calc_linkedlist(link):
    
    if link is None:
        return 0
    
    cur = link.head
    sum = 0 
    while cur is not None:
        sum *= 10
        sum += cur.value
        cur = cur.next
    
    return sum


def add_linkedlists_forward(link1, link2):
    
    sum = 0
    sum += calc_linkedlist(link1)
    sum += calc_linkedlist(link2)
    
    result = LinkedList()
    if sum == 0:
        n = Node(0)
        result.head = n
    else:   
        while sum != 0:
            n = Node(sum % 10)
            result.insert_at_head(n)
            sum = sum // 10
    
    return result


# # create 2 linked lists
# a = [1, 2]
# b = []

# d1 = LinkedList()
# d2 = LinkedList()

# for item in a:
#     n = Node(item)
#     d1.insert_at_tail(n)

# for item in b:
#     n = Node(item)
#     d2.insert_at_tail(n)

# d3 = add_linkedlists_forward(d1, d2)
# print(d3.convert_to_list())


