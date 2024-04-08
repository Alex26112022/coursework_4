import pytest

from src.vacancy import Vacancy


@pytest.fixture()
def create_vacancy_1():
    return Vacancy(123, 'python разработчик', 'Рога и Копыта',
                   'test1.ru', (10000, 30000, 'RUR'), 'Липецк',
                   'уверенные знания python', 'без опыта',
                   'частичная занятость')


@pytest.fixture()
def create_vacancy_2():
    return Vacancy(456, 'python аналитик', 'Умный программист',
                   'test2.ru', (20000, None, 'RUR'), 'Орел',
                   'коммуникабельность', 'от 1 до 3 лет',
                   'частичная занятость')


@pytest.fixture()
def create_vacancy_3():
    return Vacancy(789, 'python тестировщик', 'Тест супер',
                   'test3.ru', None, None, None,
                   None, None)
