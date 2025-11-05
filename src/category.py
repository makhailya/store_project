from typing import Iterator, List

from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


class CategoryIterator:
    """Итератор для перебора продуктов в категории."""

    def __init__(self, products: List[Product]):
        self._products = products
        self._index = 0

    def __iter__(self) -> "CategoryIterator":
        """Возвращает самого себя как итератор."""
        return self

    def __next__(self) -> Product:
        """Возвращает следующий продукт из категории."""
        if self._index < len(self._products):
            product = self._products[self._index]
            self._index += 1
            return product
        raise StopIteration


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
        if not isinstance(product, (Product, Smartphone, LawnGrass)):
            raise TypeError("Можно добавить только объекты классов Product, Smartphone или LawnGrass.")
        # ... остальной код

        # Проверка на дубликат (опционально)
        if product in self.__products:
            raise ValueError("Продукт уже добавлен в категорию.")

        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> List[Product]:
        """Возвращает список продуктов (объекты класса Product)."""
        return self.__products

    @property
    def products_str(self):
        """Возвращает список строк с описанием продуктов."""
        return [str(product) for product in self.__products]

    def __contains__(self, item: str) -> bool:
        """Позволяет проверять наличие продукта по имени."""
        return any(product.name == item for product in self.__products)

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __iter__(self) -> Iterator[Product]:
        """Позволяет итерироваться по продуктам категории."""
        return CategoryIterator(self.__products)
