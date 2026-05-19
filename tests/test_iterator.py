from src.category import Category
from src.product import Product


def test_category_iterator():
    p1 = Product("Хлеб", "Бородинский", 60, 5)
    p2 = Product("Молоко", "1л", 80, 3)
    p3 = Product("Сыр", "Российский", 300, 2)
    category = Category("Продукты", "Еда", [p1, p2, p3])

    names = [product.name for product in category]  # проверяем итерацию
    assert names == ["Хлеб", "Молоко", "Сыр"]
