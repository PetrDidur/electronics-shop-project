from src.phone import Phone

def test_phone_class():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)

    # TestCase1
    assert phone1.name == "iPhone 14"
    assert phone1.price == 120_000
    assert phone1.quantity == 5
    assert phone1.number_of_sim == 2


def test_repr():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_str():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone1) == 'iPhone 14'

def test_number_of_sim():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    phone2 = Phone("iPhone 13", 120_000, 5, 3)

    # TestCase 1
    try:
        phone1.number_of_sim = 0
    except Exception as e:
        assert str(e) == "Количество физических SIM-карт должно быть целым числом больше нуля."









