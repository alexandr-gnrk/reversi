from abc import ABCMeta, abstractmethod


class Player(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, name):
        self.name = name
        self.color = None
        self.__point = 2
    
    @abstractmethod
    def get_move(self, model):
        pass

    def inc_point(self):
        self.__point += 1

    def dec_point(self):
        self.__point -= 1

    def get_point(self):
        return self.__point