import pytest

from src.category import Category
from src.product import Product


def test_product_zero_quantity():
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Тест", "Описание", 100, 0)


def test_middle_price_empty_category():
    category = Category("Пустая", "Нет товаров")
    assert category.middle_price() == 0.0


def test_middle_price_with_products():
    product1 = Product("A", "Desc", 100, 5)
    product2 = Product("B", "Desc", 200, 3)
    category = Category("Товары", "С товарами", [product1, product2])
    assert category.middle_price() == 150.0  # (100 + 200) / 2
