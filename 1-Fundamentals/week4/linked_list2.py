
from re import L


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            print("Head Node created:", self.head.value)
            return

        node = self.head

        while node.next is not None:
            print(node.value)
            print(node.next.value)
            node = node.next

        node.next = new_node
        print("Appended new Node with value:", node.next.value)


llist = LinkedList()
obh = ["1st node", "2nd node", "3rd node", "4th node", "5th node"]
for item in obh:
    llist.append(item)
