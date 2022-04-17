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

    def prepend(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            print("Head Node created: ", self.head.value)
            return

        node = self.head
        self.head = new_node
        self.head.next = node
        print("Prepended new Head Node with value:", self.head.value)
        print("Node following Head is: ", self.head.next.value)


llist = LinkedList()
llist.prepend("First Node")
llist.prepend("Inserted New First Node")
