class Node:

    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Queue:

    def __init__(self) -> None:
        self.head = None
        self.tail = None

        self.num_nodes = 0

    def size(self):
        return self.num_nodes

    def enqueue(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.num_nodes += 1

    def dequeue(self):
        if self.head is None:
            return None

        deque_node_value = self.head.value
        self.head = self.head.next
        self.num_nodes -= 1
        return deque_node_value


queue = Queue()
queue.enqueue('a')
queue.enqueue('b')
queue.enqueue('c')

print("Pass" if (queue.size() == 3) else "Fail")

queue.enqueue('d')

print("Pass" if (queue.size() == 4) else "Fail")
