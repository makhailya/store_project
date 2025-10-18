"""
Модуль с описанием класса Category.
"""

from src.product import Product


class Category:
    """Класс, описывающий категорию товаров."""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        """
        Инициализация категории.

        :param name: Название категории
        :param description: Описание категории
        :param products: Список товаров категории
        """
        self.name = name
        self.description = description
        self.products = products

        # Увеличиваем счётчики при создании новой категории
        Category.category_count += 1
        Category.product_count += len(products)

    def __repr__(self):
        return f"<Category {self.name}: {len(self.products)} товаров>"
