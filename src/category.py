from typing import List
from src.product import Product


class Category:
    """Класс для категорий товаров"""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: List[Product] = None):
        self.name = name
        self.description = description
        self.__products = products or []  # приватный список
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: Product) -> None:
        """Добавляет товар в категорию"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Можно добавить только объект класса Product")

    @property
    def products(self) -> str:
        """Возвращает список товаров в удобном для вывода виде"""
        if not self.__products:
            return "Нет товаров"
        return "\n".join(
            f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт." for p in self.__products
        )
