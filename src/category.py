from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


class Category:
    category_count = 0
    product_count = 0  # Счётчик продуктов

    def __init__(self, name: str, description: str, products: list = None):
        self.name = name
        self.description = description
        self.__products = []  # Инициализируем пустой список
        Category.category_count += 1

        # Добавляем продукты через add_product (чтобы увеличить счётчик)
        if products:
            for product in products:
                self.add_product(product)

    def __contains__(self, item):
        if isinstance(item, str):
            return any(product.name == item for product in self.__products)
        else:
            return item in self.__products

    def add_product(self, product):
        # Проверка типа
        if not isinstance(product, (Product, Smartphone, LawnGrass)):
            raise TypeError("Можно добавить только объекты классов Product, Smartphone или LawnGrass.")

        # Проверка на дубликат
        if product in self.__products:
            return

        # Добавляем продукт
        self.__products.append(product)
        Category.product_count += 1

    def middle_price(self) -> float:
        if not self.__products:
            return 0.0
        total_price = sum(product.price for product in self.__products)
        return total_price / len(self.__products)

    def __str__(self) -> str:
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество товаров: {total_quantity} шт."

    def __iter__(self):
        return iter(self.__products)

    @property
    def products(self):
        return self.__products

    def __repr__(self):
        return f"<Category '{self.name}' with {len(self.__products)} products>"
