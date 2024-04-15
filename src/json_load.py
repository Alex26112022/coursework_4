import json
from src.load_hh import HH
from src.vacancy_json_abc import VacancyJsonAbc


class VacancyJson(VacancyJsonAbc):
    """ Работает с json-файлом. """

    def __init__(self, list_vacancies: list, path_json: str):
        self.vacancies = list_vacancies
        self.path_json = path_json

    def load_json(self):
        """ Записывает данные в Json-файл. """
        with open(self.path_json, 'w', encoding='utf-8') as file:
            json.dump(self.vacancies, file, ensure_ascii=False, indent=4)
        print('Данные успешно записаны!\n')

    def read_json(self):
        """ Считывает данные с json-файла. """
        item = None
        try:
            with open(self.path_json, encoding='utf-8') as file:
                item = json.load(file)
        except FileNotFoundError:
            print('Такого файла не существует!')
        return item

    def add_json(self, new_list):
        """ Добавляет словари в json-файл. """
        try:
            with open(self.path_json, encoding='utf-8') as file:
                data = json.load(file)
                for el in new_list:
                    data.append(el)

            with open(self.path_json, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except FileNotFoundError:
            print('Такого файла не существует!')
        print('Данные успешно добавлены!')

    def del_json(self, key_input: str, value_input: str):
        """ Удаляет словарь из json по id. """
        try:
            with open(self.path_json, encoding='utf-8') as file:
                data = json.load(file)
                for num_, el in enumerate(data):
                    if value_input == el.get(key_input):
                        data.pop(num_)

            with open(self.path_json, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except FileNotFoundError:
            print('Такого файла не существует!')
