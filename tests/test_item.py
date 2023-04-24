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





