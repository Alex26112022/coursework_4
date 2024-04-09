import json
from src.vacancy import Vacancy


class ListVacancies:
    """ Класс-генератор объектов вакансий. """
    def __init__(self, json_path):
        self.info = None
        self.json_path = json_path
        self.list_vacancies()
        self.all_vacancies = []

    def list_vacancies(self):
        """ Считывает данные с файла json. """
        with open(self.json_path, encoding='utf-8') as file:
            self.info = json.load(file)

    def generate_vacancies(self):
        """ Генерирует список объектов класса Vacancy. """
        for vacancy in self.info:
            # print(vacancy, '\n')
            vacancy_id = vacancy.get("id")
            vacancy_title = vacancy.get("name")
            vacancy_published = vacancy.get("published_at")
            vacancy_url = vacancy.get("alternate_url")
            company_name = vacancy.get("employer", {}).get("name")
            salary = vacancy.get("salary", {})
            if salary is not None:
                salary = salary.get("from"), salary.get('to'), salary.get("currency")
            address = vacancy.get("address")
            if address is not None:
                address = address.get("city")
            snippet = vacancy.get("snippet", {})
            if snippet is not None:
                snippet = snippet.get("requirement")
                if snippet is not None:
                    snippet = snippet.replace('<highlighttext>', '')
                    snippet = snippet.replace('</highlighttext>', '')
            experience = vacancy.get("experience", {})
            if experience is not None:
                experience = experience.get("name")
            employment = vacancy.get("employment", {})
            if employment is not None:
                employment = employment.get("name")

            self.all_vacancies.append(Vacancy(vacancy_id, vacancy_title,
                                              vacancy_published,
                                              company_name, vacancy_url,
                                              salary, address, snippet,
                                              experience, employment))

    def get_all_vacancies(self):
        """ Возвращает список объектов. """
        return self.all_vacancies
