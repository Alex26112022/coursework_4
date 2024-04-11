from config import vacancies_json
from src.func import max_vacancies, sort_of_vacancies, experience_input, \
    employment_input
from src.json_load import VacancyJson
from src.sort_vacancies import SortVacancies


def main():
    search_input = input('Введите поисковый запрос: \n')
    print('Задайте необходимые параметры и нажмите ENTER\n'
          'Чтобы пропустить параметр оставьте поле пустым и нажмите ENTER')
    max_count_vacancies = max_vacancies()
    type_of_sort = sort_of_vacancies()
    address_input = input('Введите адрес поиска:\n')
    input_experience = experience_input()
    input_employment = employment_input()
    input_snippet = input('Введите через пробел ключевые слова для фильтрации '
                          'вакансий по требуемым навыкам:\n').split()

    # new_search = VacancyJson(search_input)
    # new_search.load_json(vacancies_json)

    new_list = SortVacancies(vacancies_json)
    if type_of_sort == '1':
        new_list.sort_pay()
    elif type_of_sort == '2':
        new_list.sort_published()

    if bool(address_input):
        new_list.filter_address(address_input)

    if input_experience is not None:
        new_list.filter_experience(input_experience)

    if input_employment is not None:
        new_list.filter_employment(input_employment)

    if bool(input_snippet):
        for item in input_snippet:
            new_list.filter_snippet(item)

    if max_count_vacancies is not None:
        my_list = new_list.get_sort_vacancies()[:max_count_vacancies]
    else:
        my_list = new_list.get_sort_vacancies()

    for el in my_list:
        print(el)


if __name__ == '__main__':
    main()
