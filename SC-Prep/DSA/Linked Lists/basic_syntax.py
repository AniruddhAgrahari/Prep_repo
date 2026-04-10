class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next


ll = SinglyLinkedList()
ll.insert_head(10)
ll.insert_head(20)
ll.insert_head(30)
ll.print_list()