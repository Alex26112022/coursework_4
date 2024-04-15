from abc import ABC, abstractmethod


class HhAbc(ABC):
    """ Абстрактный метод класса HH. """

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def load_vacancies(self, keyword):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass
