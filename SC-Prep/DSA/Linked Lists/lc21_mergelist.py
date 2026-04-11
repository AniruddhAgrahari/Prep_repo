#Leetcode 21

class ListNode:
    def __init__(self, val = 0, next = None):
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

def merge_linked_list(list1, list2):
    
    dummy = ListNode(0)
    curr = dummy

    while list1 is not None and list2 is not None:
        if list1.val <= list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next

    if list1 is None:
        curr.next = list2
    else:
        curr.next = list1
    
    return dummy.next


assert to_list(merge_linked_list(build_list([1,2,3]), build_list([4, 5, 6]))) == [1, 2, 3, 4, 5, 6]

