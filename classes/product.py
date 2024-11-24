class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.price} руб."

    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price})"

    def __eq__(self, other):
        return self.price == other.price

    def __lt__(self, other):
        return self.price < other.price
