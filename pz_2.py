from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):

    def __init__(self, size):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size

    def consumption(self):
        res1 = round(self.__size / 6.5 + 0.5, 2)
        return res1


class Costume(Clothes):

    def __init__(self, height):
        self.__height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    def consumption(self):
        res2 = round(2 * self.__height + 0.3, 2)
        return res2


test = Coat(6.5)
test.consumption()
print(f'Для изготовления пальто  размера {test.size} необходимо {test.consumption()} ткани.')
test1 = Costume(10)
test1.consumption()
print(f'Для изготовления костюма на рост {test1.height} необходимо {test1.consumption()} ткани.')
print(f'Общий расход ткани {round(test.consumption() + test1.consumption(), 2)}')

test.size = 27
print(f'Для изготовления пальто  размера {test.size} необходимо {test.consumption()} ткани.')
test1.height = 4
print(f'Для изготовления костюма на рост {test1.height} необходимо {test1.consumption()} ткани.')
print(f'Общий расход ткани {round(test.consumption() + test1.consumption(), 2)}')
