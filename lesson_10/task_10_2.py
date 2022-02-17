from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def fabric_size(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def fabric_size(self):
        return round(self.v/6.5+0.5, 2)


class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def fabric_size(self):
        return round(2*self.h+0.3, 2)


coat_1 = Coat(25)
print(coat_1.fabric_size)
suit_1 = Suit(34)
print(suit_1.fabric_size)
