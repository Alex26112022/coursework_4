from abc import ABC, abstractmethod


class VacancyJsonAbc(ABC):
    """ Абстрактный класс работы с файлом json. """

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def load_json(self):
        pass

    @abstractmethod
    def read_json(self):
        pass

    @abstractmethod
    def add_json(self, new_list):
        pass

    @abstractmethod
    def del_json(self, key_input: str, value_input: str):
        pass
