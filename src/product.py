from src.base_product import BaseProduct
from src.mixins import CreationLoggerMixin


class Product(BaseProduct, CreationLoggerMixin):
    """
    Товар в магазине с названием, описанием, ценой и количеством.

    Атрибуты:
        _name (str): название товара
        _description (str): описание товара
        __price (float): цена товара (должна быть > 0)
        _quantity (int): количество товара на складе (должно быть > 0)
    """

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Создаёт экземпляр товара.

        Args:
            name: название товара
            description: описание товара
            price: цена товара (должен быть > 0)
            quantity: количество товара (должен быть > 0)

        Raises:
            ValueError: если price ≤ 0 или quantity ≤ 0
        """
        if quantity <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        if price <= 0:
            raise ValueError("Цена не должна быть нулевая или отрицательная")

        self._name = name
        self._description = description
        self.__price = price
        self._quantity = quantity

    @property
    def name(self) -> str:
        """Возвращает название товара."""
        return self._name

    @property
    def description(self) -> str:
        """Возвращает описание товара."""
        return self._description

    @property
    def price(self) -> float:
        """Возвращает цену товара."""
        return self.__price

    @price.setter
    def price(self, value: float):
        """
        Устанавливает новую цену товара.

        Args:
            value: новая цена (должна быть > 0)

        Raises:
            ValueError: если value ≤ 0
        """
        if value <= 0:
            raise ValueError("Цена не должна быть нулевая или отрицательная")
        self.__price = value

    @property
    def quantity(self) -> int:
        """Возвращает количество товара."""
        return self._quantity

    @quantity.setter
    def quantity(self, value: int):
        """
        Устанавливает новое количество товара.

        Args:
            value: новое количество (должно быть > 0)

        Raises:
            ValueError: если value ≤ 0
        """
        if value <= 0:
            raise ValueError("Количество должно быть положительным")
        self._quantity = value

    def __add__(self, other):
        """
        Складывает стоимость двух товаров одного типа.

        Args:
            other: другой объект Product

        Returns:
            float: суммарная стоимость (цена × количество для каждого товара)

        Raises:
            TypeError: если товары разных типов
        """
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных типов.")
        return self.price * self.quantity + other.price * other.quantity

    def __str__(self) -> str:
        """
        Возвращает строковое представление товара.

        Returns:
            str: формат "Название, цена руб. Остаток: количество шт."
        """
        return f"{self._name}, {self.price} руб. Остаток: {self.quantity} шт."

    @classmethod
    def new_product(cls, data: dict):
        """
        Создаёт новый продукт из словаря с данными.

        Args:
            data: словарь с ключами 'name', 'description', 'price', 'quantity'

        Returns:
            Product: новый экземпляр товара

        Raises:
            ValueError: если отсутствуют обязательные поля
        """
        required_fields = {"name", "description", "price", "quantity"}
        if not required_fields.issubset(data.keys()):
            raise ValueError("Отсутствуют обязательные поля для создания продукта")

        return cls(
            data["name"],
            data["description"],
            data["price"],
            data["quantity"]
        )
