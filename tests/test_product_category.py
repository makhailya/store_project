import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product_data():
    return {"name": "Хлеб", "description": "Бородинский", "price": 60.0, "quantity": 5}


def test_product_init(product_data):
    product = Product(**product_data)
    assert product.name == "Хлеб"
    assert product.price == 60.0
    assert product.quantity == 5


def test_category_add_product(product_data):
    product = Product(**product_data)
    category = Category("Продукты", "Еда")
    category.add_product(product)
    assert "Хлеб" in category  # работает через __contains__
    # Удалено: assert "60.0 руб." in category.products


def test_add_product_wrong_type():
    category = Category("Продукты", "Еда")
    with pytest.raises(TypeError, match="Можно добавить только объекты классов Product, Smartphone или LawnGrass."):
        category.add_product("не продукт")


def test_price_setter_negative(capsys):
    product = Product("Хлеб", "Бородинский", 50, 3)
    product.price = -10
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 50


def test_new_product_creates(product_data):
    product = Product.new_product(product_data)
    assert isinstance(product, Product)
    assert product.name == "Хлеб"
    assert product.price == 60.0
