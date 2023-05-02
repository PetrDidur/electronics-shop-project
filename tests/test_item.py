"""Здесь надо написать тесты с использованием pytest для модуля item."""
import os.path

from src.item import Item
from src.phone import Phone

path = os.path.join("../src/", "items.csv")
def test_item_class():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    # TestCase #1
    assert item1.name == "Смартфон"
    assert item1.price == 10_000
    assert item1.quantity == 20

    # TestCase #2
    assert item2.name == "Ноутбук"
    assert item2.price == 20_000
    assert item2.quantity == 5


def test_total_price():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert item1.calculate_total_price() == 200_000
    assert item2.calculate_total_price() == 100_000


def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    # TestCase 1
    item1.pay_rate = 0.5
    item1.apply_discount()
    assert item1.price == 5_000

    # TestCase 2
    item2.pay_rate = 0.5
    item2.apply_discount()
    assert item2.price == 10_000


def test_string_to_number():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

    # TestCase #1
    try:
        item1.name = "Очень длинное наименование товара"
    except Exception as e:
        assert str(e) == "Длина наименования товара превышает 10 символов."

    # TestCase #2
    try:
        item2.name = "Очень длинное наименование товара"
    except Exception as e:
        assert str(e) == "Длина наименования товара превышает 10 символов."


def test_instantiate_from_csv():
    products = Item.instantiate_from_csv()
    assert len(products) == 5
    assert products[0].name == "Смартфон"
    assert products[0].price == '100'
    assert products[0].quantity == 1
    assert products[1].name == "Ноутбук"
    assert products[1].price == '1000'
    assert products[1].quantity == 3
    assert products[2].name == "Кабель"
    assert products[2].price == '10'
    assert products[2].quantity == 5
    assert products[3].name == "Мышка"
    assert products[3].price == '50'
    assert products[3].quantity == 5
    assert products[4].name == "Клавиатура"
    assert products[4].price == '75'
    assert products[4].quantity == 5

def test_repr():
    # TestCase __repr__
    item3 = Item("Bazooka", 20, 1)
    assert repr(item3) == "Item('Bazooka', 20, 1)"


def test_str():
    # TestCase __str__
    item3 = Item("Bazooka", 20, 1)
    assert str(item3) == "Bazooka"


def test_add():
    item = Item("Bazooka", 20, 1)
    phone = Phone("iPhone 14", 120_000, 5, 2)

    assert item + phone == 6
