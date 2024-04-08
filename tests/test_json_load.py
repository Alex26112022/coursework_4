import pytest

from config import vacancies_json_test
from src.json_load import VacancyJson


def test_json_load(monkeypatch):
    def mock_json(a, b):
        return [
            {
                "id": "96034351",
                "name": "Junior Python",
                "salary": {
                    "from": 50000,
                    "to": 100000,
                    "currency": "RUR"
                },
                "employer": {"name": "Yakov Lushkov Neuro-Agency"},
                "address": {"city": "Москва"},
                "snippet": {"requirement": "Знание Python на базовом уровне"},
                "experience": {"name": "нет опыта"},
                "employment": {"name": "полный рабочий день"},
                "alternate_url": "https://hh.ru/vacancy/96034351"
            },
            {
                "id": "96034352",
                "name": "Python developer",
                "salary": {
                    "from": 100000,
                    "to": 200000,
                    "currency": "RUR"
                },
                "employer": {"name": "Skypro"},
                "address": {"city": "Санкт-Петербург"},
                "snippet": {"requirement": "Знание Django"},
                "experience": {"name": "от 1 до 3 лет"},
                "employment": {"name": "удаленная работа"},
                "alternate_url": "https://hh.ru/vacancy/94450348"
            }
        ]

    monkeypatch.setattr(VacancyJson, 'hh_load', mock_json)
    new_vac = VacancyJson('test')
    new_vac.load_json(vacancies_json_test)
