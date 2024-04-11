def max_vacancies():
    """ Возвращает топ N вакансий, запрашиваемых у пользователя. """
    max_count_vacancies = input('Введите количество вакансий для вывода '
                                'в топ N и нажмите ENTER!\n'
                                'Либо просто нажмите ENTER для вывода '
                                'всего списка...  ')
    if not bool(max_count_vacancies):
        max_count_vacancies = None
    else:
        while not max_count_vacancies.isdigit():
            print('Введите положительное целое число!')
            max_count_vacancies = input('Попробуйте еще раз...')
            if not bool(max_count_vacancies):
                max_count_vacancies = None
                break
        if max_count_vacancies is not None:
            max_count_vacancies = int(max_count_vacancies)

    return max_count_vacancies


def sort_of_vacancies():
    """
    Запрашивает у пользователя тип сортировки и возвращает
    соответствующий номер.
    """
    sort_input = input('Введите тип сортировки!\n\t1 - по убыванию '
                       'минимальной зарплаты\n\t2 - по дате публикации\n'
                       'Чтобы не применять сортировку просто нажмите ENTER\n')
    if bool(sort_input):
        while sort_input not in ['1', '2'] and bool(sort_input):
            sort_input = input('Выберите три варианта: "1", "2" или ENTER\n')

    return sort_input


if __name__ == '__main__':
    print(type(sort_of_vacancies()))
