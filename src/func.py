def max_vacancies():
    """ Возвращает топ N вакансий, запрашиваемых у пользователя. """
    max_count_vacancies = input('Введите количество вакансий для вывода '
                                'в топ N:\n')
    if not bool(max_count_vacancies):
        max_count_vacancies = None
    else:
        while not max_count_vacancies.isdigit():
            print('Введите положительное целое число!')
            max_count_vacancies = input('Попробуйте еще раз:\n')
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
    sort_input = input('Введите тип сортировки:\n\t1 - по убыванию '
                       'минимальной зарплаты\n\t2 - по дате публикации\n')
    if bool(sort_input):
        while sort_input not in ['1', '2'] and bool(sort_input):
            sort_input = input('Выберите один из двух вариантов: "1", "2"; '
                               'или пропустите параметр:\n')

    return sort_input


def experience_input():
    """
    Запрашивает у пользователя требуемый опыт работы и возвращает
    соответствующий ключ.
    """
    experience_dict = {'1': 'Нет опыта',
                       '2': 'От 1 года до 3 лет',
                       '3': 'От 3 до 6 лет',
                       '4': 'Более 6 лет'}
    input_experience = input('Введите требуемый опыт работы:\n'
                             '\t1 - Нет опыта\n\t2 - От 1 года до 3 лет\n'
                             '\t3 - От 3 до 6 лет\n\t4 - Более 6 лет\n')
    if bool(input_experience):
        while input_experience not in ['1', '2', '3', '4'] and bool(
                input_experience):
            input_experience = input('Выберите один из четырех вариантов: '
                                     '"1", "2", "3", "4"; '
                                     'или пропустите параметр:\n')
    return experience_dict.get(input_experience)


def employment_input():
    """
    Запрашивает у пользователя тип занятости и возвращает
    соответствующий ключ.
    """
    employment_dict = {'1': 'Полная занятость',
                       '2': 'Частичная занятость',
                       '3': 'Проектная работа',
                       '4': 'Волонтерство',
                       '5': 'Стажировка'}
    input_employment = input('Введите требуемый тип занятости:\n'
                             '\t1 - Полная занятость\n\t2 - Частичная занятость\n'
                             '\t3 - Проектная работа\n\t4 - Волонтерство\n'
                             '\t5 - Стажировка\n')
    if bool(input_employment):
        while input_employment not in ['1', '2', '3', '4', '5'] and bool(
                input_employment):
            input_employment = input('Выберите один из пяти вариантов: '
                                     '"1", "2", "3", "4", "5"; '
                                     'или пропустите параметр:\n')
    return employment_dict.get(input_employment)


if __name__ == '__main__':
    print(employment_input())
