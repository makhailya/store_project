import pytest

from src.product import Product
from src.smartphone import Smartphone


def test_product_creation_logs_output(capsys):
    product = Product("Хлеб", "Бородинский", 50.0, 5)
    captured = capsys.readouterr()
    assert "Product создан с параметрами" in captured.out
    assert product.name == "Хлеб"  # пример использования
    assert product.price == 50.0


def test_base_class_is_abstract():
    import abc

    from src.base_product import BaseProduct

    assert issubclass(BaseProduct, abc.ABC)
    with pytest.raises(TypeError):
        BaseProduct("test", "desc", 10, 2)


def test_smartphone_inherits_from_product():
    smartphone = Smartphone("iPhone", "desc", 1000, 2, 99.0, "15", 256, "серый")
    assert isinstance(smartphone, Product)
