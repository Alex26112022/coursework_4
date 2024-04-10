from src.list_vacancies import ListVacancies
from config import vacancies_json


class SortVacancies:
    """ Класс сортировки и фильтрации вакансий. """
    def __init__(self, json_path):
        new_list = ListVacancies(json_path)
        new_list.generate_vacancies()
        self.all_vacancies = new_list.get_all_vacancies()

    def sort_pay(self):
        """ Сортирует вакансии по зарплате """
        self.all_vacancies.sort(reverse=True)

    def sort_published(self):
        """ Сортирует вакансии по дате публикации. """
        self.all_vacancies.sort(key=lambda x: x.format_published(), reverse=True)

    def filter_address(self, expected_address: str):
        """ Фильтрует список по названию города. """
        filter_list = []
        for vacancy in self.all_vacancies:
            if vacancy.address.lower().strip() == expected_address.lower().strip():
                filter_list.append(vacancy)
        self.all_vacancies = filter_list

    def filter_experience(self, expected_experience):
        """ Фильтрует список по опыту работы. """
        filter_list = []
        for vacancy in self.all_vacancies:
            if vacancy.experience == expected_experience:
                filter_list.append(vacancy)
        self.all_vacancies = filter_list

    def filter_employment(self, expected_employment):
        """ Фильтрует список по типу занятости. """
        filter_list = []
        for vacancy in self.all_vacancies:
            if vacancy.employment == expected_employment:
                filter_list.append(vacancy)
        self.all_vacancies = filter_list

    def filter_snippet(self, expected_snippet: str):
        """ Фильтрует список требуемым навыкам. """
        filter_list = []
        for vacancy in self.all_vacancies:
            if expected_snippet.lower() in vacancy.snippet.lower():
                filter_list.append(vacancy)
        self.all_vacancies = filter_list

    def get_sort_vacancies(self):
        """ Возвращает отсортированный список вакансий. """
        return self.all_vacancies


fff = SortVacancies(vacancies_json)
fff.sort_pay()
# fff.sort_published()
fff.filter_address('москва')
# fff.filter_experience('От 3 до 6 лет')
fff.filter_employment('Стажировка')
fff.filter_snippet('sql')
print(len(fff.get_sort_vacancies()))
for el in fff.get_sort_vacancies():
    print(el)