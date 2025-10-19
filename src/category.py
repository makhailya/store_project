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
        """Возвращает список объектов товаров."""
        return self.__products

    @property
    def products_str(self) -> str:
        """Возвращает строку со всеми товарами (для вывода пользователю)."""
        if not self.__products:
            return "Нет товаров"
        return "\n".join(
            f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт."
            for p in self.__products
        ) + "\n"

    def __contains__(self, item: str) -> bool:
        """Позволяет проверять наличие продукта по имени через 'in'."""
        return any(product.name == item for product in self.__products)
