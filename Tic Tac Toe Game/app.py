
class Item:
    def __int__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity


item1 = Item()
print(item1.calculate_total_price("phone",200,3))





