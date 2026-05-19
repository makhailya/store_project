import pytest

from src.category import Category
from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_product_addition_same_class():
    p1 = Product("Товар1", "Описание", 100.0, 2)
    p2 = Product("Товар2", "Описание", 200.0, 3)
    assert p1 + p2 == 100.0 * 2 + 200.0 * 3


def test_product_addition_different_classes():
    p1 = Smartphone("Samsung", "Флагман", 100000.0, 2, 90, "S23", 256, "Gray")
    p2 = LawnGrass("Трава", "Газон", 500.0, 10, "Россия", "5 дней", "Зелёная")
    with pytest.raises(TypeError):
        _ = p1 + p2


def test_add_product_invalid_type():
    c = Category("Техника", "Разная техника", [])
    with pytest.raises(TypeError):
        c.add_product("not a product")


def test_product_str_and_category_str():
    p = Product("Хлеб", "Ржаной", 50.0, 10)
    c = Category("Продукты", "Еда", [p])
    assert "Хлеб" in str(p)
    assert "Продукты" in str(c)
