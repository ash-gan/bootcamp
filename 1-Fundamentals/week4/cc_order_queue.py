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


class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()

    def take_order(self, customer, flavor, scoops):
        if flavor not in self.flavors and scoops not in range(1, 4):
            print("Sorry we don't have that flavor." +
                  "\n Choose between 1-3 scoops")
        print("Order Created!")
        order = {"customer": customer, "flavor": flavor, "scoops": scoops}
        self.orders.enqueue(order)

    def show_all_orders(self):
        print("All pending Ice Cream Orders:")
        for order in self.orders.items:
            self.print_order(order)

    def print_order(self, order):
        print("Customer:", order['customer'], "--", "Flavor:",
              order['flavor'], "--", "Scoops:", order['scoops'])

    def show_next_order(self):
        next_order = self.orders.dequeue()
        print("Next order up in the queue !")
        self.print_order(next_order)


shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.show_next_order()
shop.show_all_orders()
