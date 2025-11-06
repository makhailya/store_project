from src.base_product import BaseProduct
from src.mixins import CreationLoggerMixin


class Product(CreationLoggerMixin, BaseProduct):
    """Класс, описывающий продукт."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        super().__init__(name, description, price, quantity)

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self._price = value

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных типов.")
        return self.price * self.quantity + other.price * other.quantity

    @classmethod
    def new_product(cls, data: dict):
        """Создаёт новый продукт из словаря данных."""
        required_fields = {"name", "description", "price", "quantity"}
        if not required_fields.issubset(data.keys()):
            raise ValueError("Отсутствуют обязательные поля для создания продукта")

        return cls(data["name"], data["description"], data["price"], data["quantity"])
