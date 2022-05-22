from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def add(self, title: str, quantity: int):
        """Увеличивает запас"""
        pass

    @abstractmethod
    def remove(self, title: str, quantity: int):
        """Уменьшает запас"""
        pass

    @abstractmethod
    def get_free_space(self):
        """Возвращает колличество свободных мест"""

    @abstractmethod
    def get_items(self):
        """Возвращает содержание склада в словаре"""
        pass

    def get_unique_items_count(self):
        """Возвращает колличество уникальных значений в словаре"""
        pass


class Store(Storage):
    def __init__(self):
        self.items = {}
        self.capacity = 100

    def add(self, title: str, quantity: int):
        if self.get_free_space() >= quantity:
            if title in self.items.keys():
                self.items[title] = self.items.get(title) + quantity
            else:
                self.items[title] = quantity
            return True
        else:
            print(f"Не хватает места для хранение, можно добавить только {self.get_free_space()}")

    def remove(self, title: str, quantity: int):
        if title in self.items.keys() and self.items[title] >= quantity:
            self.items[title] = self.items.get(title) - quantity
            return True
        else:
            print("Данного товара нет на складе или нет такого колличества")

    def get_free_space(self):
        quantity = 0
        for item in self.items.values():
            quantity += item
        return self.capacity - quantity

    def get_items(self):
        return self.items

    def get_unique_items_count(self):
        return len(self.items.keys())


class Shop(Store):
    def __init__(self):
        self.items = {}
        self.capacity = 20

    def add(self, title: str, quantity: int):
        if title in self.items.keys():
            super().add(title, quantity)
            return True
        elif self.get_unique_items_count() < 5:
            super().add(title, quantity)
            return True
        else:
            print("Не хватает места для хранение, можно добавить только 5 уникальных позиций")


class Request:
    def __init__(self, user_ansver):
        user_data = user_ansver.split()
        self.from_ = user_data[4]
        self.to = user_data[6]
        self.amount = int(user_data[1])
        self.product = user_data[2]

    def __repr__(self):
        return f'Доставить {self.amount} {self.product} из {self.from_} в {self.to}'
