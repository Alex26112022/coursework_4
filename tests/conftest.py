import pytest

from src.vacancy import Vacancy


@pytest.fixture()
def create_vacancy_1():
    return Vacancy(123, 'python разработчик', '2024-04-03T00:16:03+0300',
                   'Рога и Копыта',
                   'test1.ru', (10000, 30000, 'RUR'), 'Липецк',
                   'уверенные знания python', 'без опыта',
                   'частичная занятость')


@pytest.fixture()
def create_vacancy_2():
    return Vacancy(456, 'python аналитик', '2024-03-03T00:16:03+0300',
                   'Умный программист',
                   'test2.ru', (20000, None, 'RUR'), 'Орел',
                   'коммуникабельность', 'от 1 до 3 лет',
                   'частичная занятость')


@pytest.fixture()
def create_vacancy_3():
    return Vacancy(789, 'python тестировщик', '2024-02-03T00:16:03+0300',
                   'Тест супер',
                   'test3.ru', None, None, None,
                   None, None)
