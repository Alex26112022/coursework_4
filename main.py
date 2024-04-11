from config import vacancies_json
from src.func import max_vacancies, sort_of_vacancies
from src.json_load import VacancyJson
from src.sort_vacancies import SortVacancies


def main():
    search_input = input('Введите поисковый запрос: ')

    max_count_vacancies = max_vacancies()

    type_of_sort = sort_of_vacancies()

    # new_search = VacancyJson(search_input)
    # new_search.load_json(vacancies_json)

    new_list = SortVacancies(vacancies_json)
    if type_of_sort == '1':
        new_list.sort_pay()
    elif type_of_sort == '2':
        new_list.sort_published()

    if max_count_vacancies is not None:
        my_list = new_list.get_sort_vacancies()[:max_count_vacancies]
    else:
        my_list = new_list.get_sort_vacancies()

    for el in my_list:
        print(el)


if __name__ == '__main__':
    main()
