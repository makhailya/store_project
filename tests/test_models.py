import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def sample_products():
    """Фикстура для списка товаров."""
    return [
        Product("iPhone", "Смартфон Apple", 120000.0, 10),
        Product("Galaxy", "Смартфон Samsung", 90000.0, 8),
    ]


def test_product_initialization():
    """Проверяем создание продукта."""
    product = Product("MacBook", "Ноутбук Apple", 200000.0, 5)
    assert product.name == "MacBook"
    assert product.description == "Ноутбук Apple"
    assert product.price == 200000.0
    assert product.quantity == 5


def test_category_initialization(sample_products):
    """Проверяем создание категории и связь с продуктами."""
    category = Category("Смартфоны", "Мобильные устройства", sample_products)
    assert category.name == "Смартфоны"
    assert len(category.products) == 2
    assert isinstance(category.products[0], Product)


def test_category_class_attributes(sample_products):
    """Проверяем счётчики категорий и продуктов."""
    start_categories = Category.category_count
    start_products = Category.product_count

    Category("Ноутбуки", "Персональные компьютеры", sample_products)

    assert Category.category_count == start_categories + 1
    assert Category.product_count >= start_products + len(sample_products)
