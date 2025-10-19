class Product:
    """Класс для представления товара"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price  # приватный атрибут
        self.quantity = quantity

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self.__price:
            confirm = input("Цена ниже текущей. Подтвердите понижение (y/n): ")
            if confirm.lower() != "y":
                print("Изменение цены отменено")
                return

        self.__price = new_price

    @classmethod
    def new_product(cls, product_data: dict, products_list: list = None):
        """
        Создает новый товар на основе словаря.
        Если товар с таким именем уже есть, объединяет количество и выбирает более высокую цену.
        """
        name = product_data.get("name")
        description = product_data.get("description")
        price = product_data.get("price")
        quantity = product_data.get("quantity")

        if products_list:
            for p in products_list:
                if p.name == name:
                    p.quantity += quantity
                    if price > p.price:
                        p.price = price
                    return p

        return cls(name, description, price, quantity)
