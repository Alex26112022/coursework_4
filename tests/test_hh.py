import pytest
import requests

from config import vacancies_json, vacancies_json_test
from src.load_hh import HH


def test_hh(monkeypatch):
    """ Проверка парсера. """
    class MockResponse:
        def __init__(self):
            self.status_code = 200
            self.url = 'https://api.hh.ru/vacancies'
            self.headers = {'User-Agent': 'HH-User-Agent'}
            self.params = {'text': '', 'page': 0, 'per_page': 100}

        def json(self):
            return {'items': ['test1', 'test2']}

    def mock_get(url, headers, params):
        return MockResponse()

    monkeypatch.setattr(requests, 'get', mock_get)
    test_request = HH()
    test_request.load_vacancies('python developer', vacancies_json_test)
    assert len(test_request.get_vacancies()) == 40
    print(test_request)
