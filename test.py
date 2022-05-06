class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price


    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = float(value)

    def make_discount(self, discount):
        self._price*=(100-discount)/100



product1 = Product('iphone', 2000)
print(product1.price)
product1.make_discount(10)
print(product1.price)

print(vars(Product))