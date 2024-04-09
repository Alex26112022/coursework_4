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

    def get_sort_vacancies(self):
        """ Возвращает отсортированный список вакансий. """
        return self.all_vacancies


fff = SortVacancies(vacancies_json)
fff.sort_pay()
for el in fff.get_sort_vacancies():
    print(el)
