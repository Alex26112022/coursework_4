import requests

from src.hh_abc import HhAbc


class HH(HhAbc):
    """
    Класс для работы с API HeadHunter.
    """

    def __init__(self):
        self.__url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []
        print('Ждите! Идет загрузка данных...')

    def load_vacancies(self, keyword: str):
        """ Загружает данные с сайта. """
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.__url, headers=self.headers,
                                    params=self.params)
            if response.status_code == 200:
                vacancies = response.json().get("items", [])
                self.vacancies.extend(vacancies)
            else:
                print(
                    f"Request failed with status code: {response.status_code}")
            self.params['page'] += 1

    def get_vacancies(self) -> list:
        """ Возвращает список данных. """
        return self.vacancies

    def __str__(self):
        return (f'Список вакансий по запросу "{self.params['text']}"\n'
                f'Найдено вакансий...{len(self.vacancies)}')
