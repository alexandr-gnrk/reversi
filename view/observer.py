from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        pass

    @abstractmethod
    def game_over(self, subject):
        pass