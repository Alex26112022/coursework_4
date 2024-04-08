import pytest

from src.vacancy import Vacancy


def test_vacancy(create_vacancy_1, create_vacancy_2, create_vacancy_3):
    """ Проверяет инициализацию объекта вакансии. """
    print(create_vacancy_1)
    print(create_vacancy_2)
    print(create_vacancy_3)
    assert create_vacancy_1.vacancy == 'python разработчик'
    assert create_vacancy_1.pay == 10000
    assert create_vacancy_1.pay_str == 'От 10000 до 30000 RUR'
    assert create_vacancy_2.address == 'Орел'
    assert create_vacancy_3.pay == 0
    assert create_vacancy_3.pay_str == 'не указана'
    assert create_vacancy_3.snippet == 'не указаны'
    assert create_vacancy_3.experience == 'не указан'
    assert create_vacancy_3.employment == 'не указан'

