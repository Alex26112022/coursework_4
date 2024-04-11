import pytest

from config import all_vacancies_json_test
from src.sort_vacancies import SortVacancies


def test_sort_vacancies():
    """ Проверяет класс сортировки и фильтрации списка вакансий. """
    new_sort = SortVacancies(all_vacancies_json_test)
    new_sort.sort_published()
    new_sort.sort_pay()
    new_sort.filter_address('Москва')
    new_sort.filter_experience('От 3 до 6 лет')
    new_sort.filter_snippet('опыт')
    new_sort.filter_employment('Полная занятость')
    new_sort.filter_pay(50000, 250000)

    assert len(new_sort.get_sort_vacancies()) == 3
    assert new_sort.get_sort_vacancies()[0] > new_sort.get_sort_vacancies()[1]
    for el in new_sort.get_sort_vacancies():
        print(el)
