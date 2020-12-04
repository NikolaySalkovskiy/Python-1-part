from abc import ABC, abstractmethod


class Wear(ABC):

    @abstractmethod
    def consumption(self):
        """Формулы подсчета расхода ткани"""
        return 1


class Coat(Wear, ABC):

    def __init__(self, size):
        super().__init__()
        self.size = size

    @property
    def consumption(self):
        return round(self.size / 6.5 + 0.5, 2)


class Suit(Wear, ABC):

    def __init__(self, height):
        super().__init__()
        self.height = height

    @property
    def consumption(self):
        return round(2 * self.height + 0.3, 2)


# Выбор для пользователя

decide = input('Пальто или костюм?: ')
if decide.lower() == 'пальто':
    size_of_coat = int(input('Введите размер: '))
    coat = Coat(size_of_coat)
    print(f'Для пальто вашего размера необходимо {coat.consumption} единиц ткани')
elif decide.lower() == 'костюм':
    size_of_suit = int(input('Введите рост костюма: '))
    suit = Suit(size_of_suit)
    print(f'Для вашего костюма необходимо {suit.consumption} единиц ткани')
