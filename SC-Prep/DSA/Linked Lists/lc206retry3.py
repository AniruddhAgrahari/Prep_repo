#time complexity: O(n)
#space complexity: O(1) - only 3 pointers no extra space


def reversedlinkedlist(head):

    prev = None
    curr = head
    next_node = None

    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev