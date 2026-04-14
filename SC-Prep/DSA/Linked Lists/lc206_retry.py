
# TC: O(n) - visit every node once
# SC: O(1) - only 3 pointers, no extra space


def reverse_list(head):

    prev = None
    curr = head
    next_node = None

    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev
