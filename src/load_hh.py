from pprint import pprint

import requests
from random import randint
import time


class HH:
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def load_vacancies(self, keyword):
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

    def get_vacancies(self):
        return self.vacancies

    def __str__(self):
        return (f'Список вакансий по запросу "{self.params['text']}"\n'
                f'Найдено вакансий...{len(self.vacancies)}')
