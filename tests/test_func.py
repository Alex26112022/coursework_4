import pytest
import os
from io import StringIO
from src.func import *


def test_max_vacancies(monkeypatch):
    """ Тестирует функцию, принимающую от пользователя топ N вакансий. """
    number_inputs = StringIO('5\n10\n\n')
    monkeypatch.setattr('sys.stdin', number_inputs)
    assert max_vacancies() == 5
    assert max_vacancies() == 10
    assert max_vacancies() is None


def test_sort_of_vacancies(monkeypatch):
    """ Тестирует функцию, принимающую от пользователя тип сортировки. """
    number_inputs = StringIO('1\n2\n\n')
    monkeypatch.setattr('sys.stdin', number_inputs)
    assert sort_of_vacancies() == '1'
    assert sort_of_vacancies() == '2'
    assert sort_of_vacancies() == ''


def test_experience_input(monkeypatch):
    """ Тестирует функцию, принимающую от пользователя опыт работы. """
    number_inputs = StringIO('1\n2\n3\n4\n\n')
    monkeypatch.setattr('sys.stdin', number_inputs)
    assert experience_input() == 'Нет опыта'
    assert experience_input() == 'От 1 года до 3 лет'
    assert experience_input() == 'От 3 до 6 лет'
    assert experience_input() == 'Более 6 лет'
    assert experience_input() is None


def test_employment_input(monkeypatch):
    """ Тестирует функцию, принимающую от пользователя тип занятости. """
    number_inputs = StringIO('1\n2\n3\n4\n5\n\n')
    monkeypatch.setattr('sys.stdin', number_inputs)
    assert employment_input() == 'Полная занятость'
    assert employment_input() == 'Частичная занятость'
    assert employment_input() == 'Проектная работа'
    assert employment_input() == 'Волонтерство'
    assert employment_input() == 'Стажировка'
    assert employment_input() is None


def test_schedule_input(monkeypatch):
    """ Тестирует функцию, принимающую от пользователя график работы. """
    number_inputs = StringIO('1\n2\n3\n4\n5\n\n')
    monkeypatch.setattr('sys.stdin', number_inputs)
    assert schedule_input() == 'Полный день'
    assert schedule_input() == 'Сменный график'
    assert schedule_input() == 'Гибкий график'
    assert schedule_input() == 'Удаленная работа'
    assert schedule_input() == 'Вахтовый метод'
    assert schedule_input() is None


def test_pay_input(monkeypatch):
    """ Тестирует функцию, принимающую от пользователя график работы. """
    number_inputs = StringIO('30000 60000\n50000 20000\n400000\n'
                             'test 70000\ntest1 test2\n\n')
    monkeypatch.setattr('sys.stdin', number_inputs)
    assert pay_input() == (30000.0, 60000.0)
    assert pay_input() == (50000.0, None)
    assert pay_input() == (400000.0, None)
    assert pay_input() == (None, 70000.0)
    assert pay_input() == (None, None)
    assert pay_input() is None
