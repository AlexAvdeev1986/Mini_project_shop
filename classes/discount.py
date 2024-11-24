class Discount:
    def __init__(self, description, discount_percent):
        self.description = description
        self.discount_percent = discount_percent

    @staticmethod
    def apply_discount(price, discount_percent):
        return price * (1 - discount_percent / 100)

    @staticmethod
    def seasonal_discount(order):
        return sum(Discount.apply_discount(product.price, 10) for product in order.products)  # Сезонная скидка 10%

    @staticmethod
    def promo_code_discount(order, promo_percent):
        return sum(Discount.apply_discount(product.price, promo_percent) for product in order.products)
