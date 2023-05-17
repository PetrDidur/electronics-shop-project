from src.item import Item, InstantiateCSVError
import os
path = os.path.join("../src/", "items.csv")

if __name__ == '__main__':
    # Файл items.csv отсутствует.
    print(Item.instantiate_from_csv(path))
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле items.csv удалена последняя колонка.
    Item.instantiate_from_csv(path)
    # InstantiateCSVError: Файл item.csv поврежден
