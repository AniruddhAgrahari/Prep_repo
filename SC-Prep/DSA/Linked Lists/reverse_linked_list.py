# Leetcode 206
# Time Complexity - O(n)
# Space Complexity - O(1)



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_list(values):
        if not values:
            return None
        head = ListNode(values[0])
        curr = head
        for val in values[1:]:
            curr.next = ListNode(val)
            curr = curr.next
        return head
    
def to_list(head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result

def reverse_linked_list(head):

        curr = head
        prev = None

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev
    
assert to_list(reverse_linked_list(build_list([1,2,3]))) == [3,2,1]

assert to_list(reverse_linked_list(build_list([10, 40, 60]))) == [60, 40, 10]

assert to_list(reverse_linked_list(build_list([99, 101, 504, 708]))) == [708, 504, 101, 99]
