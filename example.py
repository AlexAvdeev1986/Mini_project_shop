# Пример использования статических методов и методов класса в интернет-магазине
# Предположим, у нас есть интернет-магазин с классом Product, который представляет товар, и классом Order, который представляет заказ. 
# Мы будем использовать статические методы для расчета скидок и методы класса для подсчета общего количества заказов.
from classes.order import Order
from classes.product import Product
from classes.discount import Discount


class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def total_spent(self):
        return sum(order.total_price() for order in self.orders)

    def __str__(self):
        return f"Клиент {self.name}, общая сумма заказов: {self.total_spent()} руб."

    def __repr__(self):
        return f"Customer(name='{self.name}', orders={self.orders})"


# Тестирование реализации
if __name__ == "__main__":
    # Создание продуктов
    product1 = Product("Ноутбук", 50000)
    product2 = Product("Смартфон", 20000)
    product3 = Product("Наушники", 3000)

    # Создание клиентов
    customer1 = Customer("Иван")
    customer2 = Customer("Мария")

    # Создание заказов
    order1 = Order([product1, product3])
    order2 = Order([product2])
    order3 = Order([product1, product2, product3])

    # Добавление заказов клиентам
    customer1.add_order(order1)
    customer1.add_order(order2)
    customer2.add_order(order3)

    # Применение скидок
    print("Цена заказа с сезонной скидкой (10%):", Discount.seasonal_discount(order1))
    print("Цена заказа с промокодом (15%):", Discount.promo_code_discount(order2, 15))

    # Общая информация о клиентах и заказах
    print("\n--- Информация о клиентах ---")
    print(customer1)
    print(customer2)

    # Общая статистика
    print("\n--- Статистика заказов ---")
    print(f"Общее количество заказов: {Order.total_orders()}")
    print(f"Общая сумма всех заказов: {Order.total_value()} руб.")