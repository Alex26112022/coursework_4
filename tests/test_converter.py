import pytest
from src.valuta import converter
from config import valuta_json


def test_converter():
    """ Проверка конвертора валют. """
    assert converter(valuta_json, 'EUR') == (1, 100.7473)
    assert converter(valuta_json, 'usd') == (1, 92.7463)
    assert converter(valuta_json, 'test') == (1, 1)

