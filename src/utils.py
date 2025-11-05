import json

from src.category import Category
from src.product import Product


def load_from_json(filepath: str) -> list[Category]:
    """
    Загружает категории и продукты из JSON-файла.
    Если ключ отсутствует или значение некорректно — пропускает элемент.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    categories = []
    for cat in data:
        # Проверяем наличие обязательных полей категории
        if "name" not in cat or "description" not in cat:
            continue  # Пропускаем некорректную категорию

        # Обрабатываем продукты: пропускаем те, у которых нет обязательных полей
        products = []
        if "products" in cat and isinstance(cat["products"], list):
            for p in cat["products"]:
                if all(key in p for key in ["name", "description", "price", "quantity"]):
                    try:
                        product = Product(
                            p["name"],
                            p["description"],
                            float(p["price"]),  # Приводим к float
                            int(p["quantity"]),  # Приводим к int
                        )
                        products.append(product)
                    except (ValueError, TypeError):
                        continue  # Пропускаем продукт с некорректными числовыми значениями

        categories.append(Category(cat["name"], cat["description"], products))
    return categories
