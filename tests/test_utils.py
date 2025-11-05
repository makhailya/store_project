import json

import pytest

from src.utils import load_from_json


# Временная директория для тестов
@pytest.fixture
def temp_dir(tmp_path):
    return tmp_path


# Пример корректных данных для JSON
@pytest.fixture
def valid_json_data():
    return [
        {
            "name": "Продукты",
            "description": "Еда и напитки",
            "products": [
                {"name": "Хлеб", "description": "Бородинский", "price": 60.0, "quantity": 5},
                {"name": "Молоко", "description": "Пастеризованное", "price": 80.0, "quantity": 3},
            ],
        },
        {
            "name": "Электроника",
            "description": "Гаджеты",
            "products": [{"name": "Смартфон", "description": "iPhone 15", "price": 100000.0, "quantity": 2}],
        },
    ]


def test_load_from_json_missing_products_key(temp_dir):
    json_file = temp_dir / "no_products.json"
    data = [{"name": "Без продуктов", "description": "Нет товаров"}]
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    categories = load_from_json(str(json_file))
    assert len(categories) == 1
    assert categories[0].name == "Без продуктов"
    assert len(categories[0].products) == 0  # Пустой список продуктов


def test_load_from_json_product_missing_fields(temp_dir):
    json_file = temp_dir / "incomplete_product.json"
    data = [
        {
            "name": "Ошибка",
            "description": "Неполный продукт",
            "products": [{"name": "Нет цены", "description": "Без цены", "quantity": 1}],  # Нет "price"
        }
    ]
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    categories = load_from_json(str(json_file))
    assert len(categories) == 1
    assert len(categories[0].products) == 0  # Продукт пропущен


def test_load_from_json_invalid_price_type(temp_dir):
    json_file = temp_dir / "invalid_price.json"
    data = [
        {
            "name": "Категория",
            "description": "С ошибкой",
            "products": [{"name": "Товар", "description": "Цена строка", "price": "не число", "quantity": 1}],
        }
    ]
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    categories = load_from_json(str(json_file))
    assert len(categories) == 1
    assert len(categories[0].products) == 0  # Продукт пропущен из-за ошибки в price


def test_load_from_json_missing_category_fields(temp_dir):
    json_file = temp_dir / "missing_fields.json"
    data = [
        {"description": "Нет name"},  # Пропущен name
        {"name": "Нет description"},  # Пропущен description
        {"name": "Нормальная", "description": "Всё есть", "products": []},
    ]
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    categories = load_from_json(str(json_file))
    assert len(categories) == 1  # Только третья категория валидна
    assert categories[0].name == "Нормальная"
