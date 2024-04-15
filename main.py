from config import vacancies_json
from src.func import pay_input, schedule_input, employment_input, \
    experience_input, sort_of_vacancies, max_vacancies
from src.json_worker import VacancyJson
from src.load_hh import HH
from src.push_excel import PushExcel
from src.sort_vacancies import SortVacancies


first_run = 1
search_input = input('Введите поисковый запрос: \n')
# Парсим данные
new_search = HH()
new_search.load_vacancies(search_input)
print(new_search)
# Загружаем данные в json.
new_info = VacancyJson(new_search.get_vacancies(), vacancies_json)
new_info.load_json()

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

    print(f'\nПо данным критериям отобрано вакансий: {len(my_list)}')

    # Запись в Excel.
    new_excel_file = PushExcel(my_list)
    if first_run == 1:
        new_excel_file.push_excel()
    else:
        new_excel_file.add_excel()


def refactor():
    """ Дополнительная обработка результата. """
    global first_run
    run = True
    while run:
        user_input_1 = input('Для выхода из программы нажмите Enter...\n'
                             'Для коррекции данных введите любой символ и нажмите Enter...\n')
        if user_input_1 == '':
            run = False
        else:
            print('Выберите действие:\n\t1. Добавить данные\n\t2. Удалить '
                  'данные\n')
            user_input_2 = input()
            if user_input_2 == '1':
                add_search_input = input('Введите новый поисковый запрос: \n')
                add_search = HH()
                add_search.load_vacancies(add_search_input)
                print(add_search)
                new_info.add_json(add_search.get_vacancies())
                first_run = 2
                main()
            elif user_input_2 == '2':
                key_input = 'id'
                del_input = input('Введите id вакансии, которую необходимо '
                                  'удалить\n')
                new_info.del_json(key_input, del_input)
                del_xlsx = PushExcel([])
                del_xlsx.del_excel(del_input)
            else:
                continue


if __name__ == '__main__':
    main()
    refactor()
