import json

import requests

from config import valuta_json


def json_valuta(json_path):
    """
    Получает актуальные данные о курсах валют с API Центробанка
    и записывает их в json-файл.
    """
    with open(json_path, 'w', encoding='utf-8') as file:
        response = requests.get(
            'https://www.cbr-xml-daily.ru/daily_json.js').json()
        json.dump(response, file, indent=4)


def converter(json_path, money):
    """ Конвертирует валюту. """
    with open(json_path, encoding='utf-8') as file:
        data = json.load(file)
        item = data['Valute'].get(f'{money.upper()}')
        if item is not None:
            result = item.get('Nominal'), item.get('Value')
            return result

        return 1, 1
