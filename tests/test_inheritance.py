import pytest

from src.category import Category
from src.lawn_grass import LawnGrass
from src.smartphone import Smartphone


def test_smartphone_creation():
    phone = Smartphone("iPhone 15", "Apple", 120000, 5, "A16 Bionic", "Pro", 256, "черный")
    assert phone.model == "Pro"
    assert phone.memory == 256
    assert phone.color == "черный"


def test_lawn_grass_creation():
    grass = LawnGrass("Royal Grass", "Семена", 500, 100, "Голландия", 10, "зеленый")
    assert grass.country == "Голландия"
    assert grass.germination_period == 10


def test_add_same_type_products():
    phone1 = Smartphone("Galaxy S24", "Samsung", 100000, 2, "Snapdragon", "S24", 512, "синий")
    phone2 = Smartphone("Galaxy S25", "Samsung", 110000, 1, "Snapdragon", "S25", 1024, "черный")
    assert phone1 + phone2 == (100000 * 2 + 110000 * 1)


def test_add_different_type_products():
    phone = Smartphone("iPhone", "Apple", 100000, 2, "A16", "Pro", 256, "черный")
    grass = LawnGrass("Grass", "Семена", 500, 10, "Россия", 7, "зеленый")
    with pytest.raises(TypeError):
        _ = phone + grass


def test_add_non_product_to_category():
    category = Category("Товары", "Все товары")
    with pytest.raises(TypeError):
        category.add_product("не продукт")
