import pytest
from unittest.mock import patch
from src.product import Product
from src.category import Category


@pytest.fixture
def product_data():
    return {"name": "Молоко", "description": "1 литр", "price": 80.0, "quantity": 10}


def test_product_initialization(product_data):
    product = Product(**product_data)
    assert product.name == "Молоко"
    assert product.price == 80.0
    assert product.quantity == 10


def test_category_add_product(product_data):
    product = Product(**product_data)
    category = Category("Продукты", "Питание")
    category.add_product(product)
    assert "Молоко" in category.products


def test_add_product_wrong_type():
    category = Category("Продукты", "Питание")
    with pytest.raises(TypeError):
        category.add_product("не продукт")


def test_price_setter_invalid():
    product = Product("Молоко", "1 литр", 50, 5)
    product.price = -10
    assert product.price == 50


@patch("builtins.input", return_value="n")
def test_price_setter_decline(mock_input):
    product = Product("Молоко", "1 литр", 100, 10)
    product.price = 50
    assert product.price == 100


@patch("builtins.input", return_value="y")
def test_price_setter_confirm(mock_input):
    product = Product("Молоко", "1 литр", 100, 10)
    product.price = 50
    assert product.price == 50


def test_new_product_creates(product_data):
    product = Product.new_product(product_data)
    assert isinstance(product, Product)
    assert product.name == "Молоко"


def test_new_product_merges_existing(product_data):
    p1 = Product("Молоко", "1 литр", 80, 10)
    new_data = {"name": "Молоко", "description": "новое", "price": 100, "quantity": 5}
    p2 = Product.new_product(new_data, [p1])
    assert p1 is p2
    assert p1.quantity == 15
    assert p1.price == 100
