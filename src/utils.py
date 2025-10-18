import json
from src.category import Category
from src.product import Product


def load_from_json(filepath: str) -> list[Category]:
    """
    Загружает категории и продукты из JSON-файла.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    categories = []
    for cat in data:
        products = [
            Product(p["name"], p["description"], p["price"], p["quantity"])
            for p in cat["products"]
        ]
        categories.append(Category(cat["name"], cat["description"], products))
    return categories
