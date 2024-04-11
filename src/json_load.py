import json
from src.load_hh import HH


class VacancyJson:
    """ Записывает данные в json-файл. """

    def __init__(self, search_vacancy: str):
        self.vacancies = self.hh_load(search_vacancy)

    @staticmethod
    def hh_load(search_vacancy):
        """ Парсит вакансии с сайта. """
        hh = HH()
        hh.load_vacancies(search_vacancy)
        vacancies = hh.get_vacancies()
        print(hh)
        return vacancies

    def load_json(self, path_json):
        """ Записывает данные в Json-файл. """
        with open(path_json, 'w', encoding='utf-8') as file:
            json.dump(self.vacancies, file, indent=4)
        print('Данные успешно записаны!\n')
