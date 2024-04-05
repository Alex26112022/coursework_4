from pprint import pprint

import requests
from random import randint
import time
import json

from config import vacancies_json


class HH:
    """
    Класс для работы с API HeadHunter.
    Стягивает данные с сайта и записывает их в json-файл.
    """

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def load_vacancies(self, keyword, path_vacancies):
        """ Загружает данные с сайта. """
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            # time.sleep(randint(1, 4))
            response = requests.get(self.url, headers=self.headers,
                                    params=self.params)
            if response.status_code == 200:
                vacancies = response.json().get("items", [])
                self.vacancies.extend(vacancies)
            else:
                print(
                    f"Request failed with status code: {response.status_code}")
            self.params['page'] += 1

        self.load_json(path_vacancies)

    def get_vacancies(self):
        """ Возвращает список данных. """
        return self.vacancies

    def load_json(self, path_vacancies):
        """ Записывает данные в Json-файл. """
        with open(path_vacancies, 'w', encoding='utf-8') as file:
            json.dump(self.vacancies, file, indent=4)

    def __str__(self):
        return (f'Список вакансий по запросу "{self.params['text']}"\n'
                f'Найдено вакансий...{len(self.vacancies)}')
