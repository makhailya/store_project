"""
Модуль с описанием класса Product.
"""


class Product:
    """Класс, описывающий товар."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализация продукта.

        :param name: Название товара
        :param description: Описание товара
        :param price: Цена товара
        :param quantity: Количество на складе
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"<Product {self.name} ({self.price}₽, {self.quantity} шт.)>"
