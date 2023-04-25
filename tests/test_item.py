"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_item_class():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    assert item1.name == "Смартфон"
    assert item1.price == 10_000
    assert item1.quantity == 20

    assert item1.calculate_total_price() == 200000

    item1.pay_rate = 0.5
    item1.apply_discount()
    assert item1.price == 5_000

    assert item2.name == "Ноутбук"
    assert item2.price == 20_000
    assert item2.quantity == 5

    assert item2.calculate_total_price() == 100000

    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

    try:
        item1.name = "Очень длинное наименование товара"
    except Exception as e:
        assert str(e) == "Длина наименования товара превышает 10 символов."

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







