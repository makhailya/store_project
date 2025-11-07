import json
from src.product import Product
import src

def load_from_json(filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    categories = []
    for item in data:
        name = item.get("name")
        description = item.get("description")

        # Пропускаем категории без name или description
        if name is None or description is None:
            continue

        products_data = item.get("products", [])
        category = src.Category(name, description)

        for product_data in products_data:
            try:
                required_fields = {"name", "description", "price", "quantity"}
                if not required_fields.issubset(product_data.keys()):
                    continue

                price = product_data["price"]
                if not isinstance(price, (int, float)) or price <= 0:
                    continue

                product = Product(
                    product_data["name"],
                    product_data["description"],
                    price,
                    product_data["quantity"]
                )
                category.add_product(product)
            except (ValueError, TypeError):
                continue

        categories.append(category)
    return categories
