from src.base_product import BaseProduct
from src.mixins import CreationLoggerMixin

class Product(BaseProduct, CreationLoggerMixin):
    def __init__(self, name: str, description: str, price: float, quantity: int):
        if quantity <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self._name = name
        self._description = description
        self.__price = price
        self._quantity = quantity

    @property
    def name(self) -> str:
        return self._name

    @property
    def quantity(self) -> int:
        return self._quantity

    @quantity.setter
    def quantity(self, value: int):
        if value <= 0:
            raise ValueError("Количество должно быть положительным")
        self._quantity = value

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = value

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных типов.")
        return self.price * self.quantity + other.price * other.quantity

    def __str__(self) -> str:
        return f"{self._name}, {self.price} руб. Остаток: {self.quantity} шт."

    @classmethod
    def new_product(cls, data: dict):
        required_fields = {"name", "description", "price", "quantity"}
        if not required_fields.issubset(data.keys()):
            raise ValueError("Отсутствуют обязательные поля для создания продукта")
        return cls(
            data["name"],
            data["description"],
            data["price"],
            data["quantity"]
        )

    @property
    def description(self) -> str:
        return self._description
