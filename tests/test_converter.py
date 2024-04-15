from src.valuta import converter
from config import valuta_json_test


def test_converter():
    """ Проверка конвертора валют. """
    assert converter(valuta_json_test, 'EUR') == (1, 100.7473)
    assert converter(valuta_json_test, 'usd') == (1, 92.7463)
    assert converter(valuta_json_test, 'test') == (1, 1)
