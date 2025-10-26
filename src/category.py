from typing import List
from src.product import Product


class Category:
    """Класс, описывающий категорию товаров."""

    category_count = 0
    product_count = 0


    def __init__(self, name: str, description: str, products: List[Product] = None):
        self.name = name
        self.description = description
        self.__products = products or []
        Category.category_count += 1
        Category.product_count += len(self.__products)


    def add_product(self, product: Product) -> None:
        """Добавление продукта в категорию."""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Можно добавить только объект класса Product")

    @property
    def products(self) -> List[Product]:
        """Возвращает список продуктов."""
        return self.__products

    @property
    def products_str(self) -> str:
        """Возвращает строковое представление всех товаров."""
        return "\n".join(str(p) for p in self.__products) + "\n"


    def __contains__(self, item: str) -> bool:
        """Позволяет проверять наличие продукта по имени."""
        return any(product.name == item for product in self.__products)


    def __str__(self) -> str:
        """Строковое представление категории."""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
