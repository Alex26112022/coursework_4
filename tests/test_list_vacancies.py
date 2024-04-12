import pytest
from config import vacancies_json_test
from src.list_vacancies import ListVacancies


def test_list_vacancies():
    """ Проверяет генератор списка объектов вакансий. """
    new_list = ListVacancies(vacancies_json_test)
    new_list.generate_vacancies()
    assert len(new_list.get_all_vacancies()) == 2
    print(new_list.get_all_vacancies()[0])
    print(new_list.get_all_vacancies()[1])
    assert new_list.get_all_vacancies()[0].vacancy == 'Junior Python'
    assert new_list.get_all_vacancies()[1].pay_min == 100000
    assert new_list.get_all_vacancies()[1].pay_str == 'От 100000 до 200000 RUR'

