import csv
import os

path = os.path.join("../src/", "items.csv")


class InstantiateCSVError(Exception):
    pass


class Item:

    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__()
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        return self.quantity + other.quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.quantity * self.price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            raise Exception('Длина наименования товара превышает 10 символов.')
        self.__name = name

    @classmethod
    def instantiate_from_csv(cls, path):
        try:
            with open(path, newline='', encoding="utf-8") as csvfile:
                data = csv.DictReader(csvfile)
                for row in data:
                        name = row['name']
                        price = row['price']
                        quantity = int(row['quantity'])
                        item = cls(name, price, quantity)
                        cls.all.append(item)
        except KeyError:
            raise InstantiateCSVError("Файл поврежден")
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")

        return cls.all

    @staticmethod
    def string_to_number(string: str):
        try:
            return int(string)
        except ValueError:
            num = int(string[0])
            return num


class LanguageMixin:
    def __init__(self):
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.language == 'EN':
            self.__language = 'RU'
            return self
        elif self.language == 'RU':
            self.__language = 'EN'
            return self


class Keyboard(Item, LanguageMixin):
    def __init__(self, name, price: float, quantity: int):
        super().__init__(name, price, quantity)

