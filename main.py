from config import vacancies_json
from src.func import *
from src.json_load import VacancyJson
from src.push_excel import PushExcel
from src.sort_vacancies import SortVacancies

search_input = input('Введите поисковый запрос: \n')

# Загружает данные в json.
new_search = VacancyJson(search_input)
new_search.load_json(vacancies_json)

print('Задайте необходимые параметры и нажмите ENTER\n'
      'Чтобы пропустить параметр оставьте поле пустым и нажмите ENTER')


def main():
    """ Главная функция. Забирает данные с json, работает с пользователем. """
    max_count_vacancies = max_vacancies()
    type_of_sort = sort_of_vacancies()
    address_input = input('Введите адрес поиска:\n')
    input_experience = experience_input()
    input_employment = employment_input()
    input_schedule = schedule_input()
    input_snippet = input('Введите через пробел ключевые слова для фильтрации '
                          'вакансий по требуемым навыкам:\n').split()
    input_pay = pay_input()

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

    if input_schedule is not None:
        new_list.filter_schedule(input_schedule)

    if bool(input_snippet):
        for item in input_snippet:
            new_list.filter_snippet(item)

    if input_pay is not None:
        if input_pay[0] is not None and input_pay[1] is not None:
            new_list.filter_pay(input_pay[0], input_pay[1])
        elif input_pay[0] is not None and input_pay[1] is None:
            new_list.filter_pay(input_pay[0])
        elif input_pay[0] is None and input_pay[1] is not None:
            new_list.filter_pay(0, input_pay[1])

    if max_count_vacancies is not None:
        my_list = new_list.get_sort_vacancies()[:max_count_vacancies]
    else:
        my_list = new_list.get_sort_vacancies()

    for el in my_list:
        print(el)

    # Запись в Excel.
    new_excel_file = PushExcel(my_list)
    new_excel_file.push_excel()


if __name__ == '__main__':
    main()
