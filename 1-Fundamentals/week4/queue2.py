class Queue:

    def __init__(self) -> None:
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if len(self.items) == 0:
            return None
        return self.items.pop(0)

    def show_queue(self):
        print(self.items)


q = Queue()
q.enqueue('a')
q.enqueue('b')
q.enqueue('c')

print("Pass" if len(q.items) == 3 else "Fail")
q.enqueue('d')
q.show_queue()
print("Pass" if len(q.items) == 4 else "Fail")
print("Pass" if q.dequeue() == 'a' else "Fail")
print("Pass" if q.dequeue() == 'b' else "Fail")
q.show_queue()
print("Pass" if q.dequeue() == 'c' else "Fail")
print("Pass" if q.dequeue() == 'd' else "Fail")
