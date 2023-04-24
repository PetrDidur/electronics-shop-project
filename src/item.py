import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

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
        if len(name) <= 10:
            self.__name = name
            return self.__name
        return "Длина имени не должна превышать 10 символов"



    @classmethod
    def instantiate_from_csv(cls):
        with open("../src/items.csv", newline='') as csvfile:
                data = csv.DictReader(csvfile)
                for row in data:
                    name = row['name']
                    price = row['price']
                    quantity = int(row['quantity'])
                    item = cls(name, price, quantity)
                    cls.all.append(item)
        return cls.all

    @staticmethod
    def string_to_number(string: str):
        try:
            return int(string)
        except ValueError:
            num = int(string[0])
            return num







    def __repr__(self):
        return f"{self.__name}, {self.price}, {self.quantity}"






