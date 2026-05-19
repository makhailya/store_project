class Product:
    """Класс, описывающий товар."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price  # ✅ приватный атрибут
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Геттер возвращает цену."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер проверяет цену и при необходимости запрашивает подтверждение."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = new_price

    @classmethod
    def new_product(cls, product_data: dict):
        """Создает новый объект Product из словаря."""
        return cls(
            name=product_data.get("name"),
            description=product_data.get("description"),
            price=product_data.get("price"),
            quantity=product_data.get("quantity"),
        )
