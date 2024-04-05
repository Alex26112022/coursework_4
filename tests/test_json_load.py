import pytest

from config import vacancies_json_test
from src.json_load import VacancyJson


def test_json_load(monkeypatch):
    def mock_json(a, b):
        return [
            {
                "id": "96034351", "name": "Junior Python", "salary": {
                    "from": 50000,
                    "currency": "RUR"},
                "alternate_url": "https://hh.ru/vacancy/96034351"}]

    monkeypatch.setattr(VacancyJson, 'hh_load', mock_json)
    new_vac = VacancyJson('test')
    new_vac.load_json(vacancies_json_test)
