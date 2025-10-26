from src.product import Product
from src.category import Category
import pytest


def test_product_str():
    p = Product("Молоко", "1л", 90.5, 10)
    assert str(p) == "Молоко, 90.5 руб. Остаток: 10 шт."


def test_category_str():
    p1 = Product("Хлеб", "Бородинский", 60, 5)
    p2 = Product("Молоко", "1л", 80, 3)
    c = Category("Продукты", "Еда", [p1, p2])
    assert "Продукты, количество продуктов: 8 шт." == str(c)


def test_product_addition():
    p1 = Product("Молоко", "1л", 100, 10)
    p2 = Product("Хлеб", "Бородинский", 50, 2)
    total = p1 + p2
    assert total == 100 * 10 + 50 * 2


def test_product_add_wrong_type():
    p = Product("Молоко", "1л", 90, 10)
    with pytest.raises(TypeError):
        _ = p + 5
