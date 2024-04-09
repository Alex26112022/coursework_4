import json

import requests


def json_valuta():
    """ Записывает данные курсов валют в json-файл. """
    with open('valuta.json', 'w', encoding='utf-8') as file:
        data = requests.get(
            'https://www.cbr-xml-daily.ru/daily_json.js').json()
        json.dump(data, file, indent=4)


def converter(money):
    """ Конвертирует валюту. """
    with open('valuta.json', encoding='utf-8') as file:
        data = json.load(file)
        item = data['Valute'].get(f'{money.upper()}')
        if item is not None:
            result = item.get('Nominal'), item.get('Value')
            return result

        return 1, 1
