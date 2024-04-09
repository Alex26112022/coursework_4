from config import valuta_json
from src.valuta import converter
from datetime import datetime


class Vacancy:
    """ Класс экземпляра вакансии. """

    def __init__(self, id_, vacancy, published, company, url, pay, address,
                 snippet, experience, employment, json_path=valuta_json):
        self.id_ = id_
        self.vacancy = vacancy
        self.published = published
        self.company = company
        self.url = url
        self.pay, self.pay_str = self.validator_pay(pay, json_path)
        if address is None:
            self.address = 'не указан'
        else:
            self.address = address
        if snippet is None:
            self.snippet = 'не указаны'
        else:
            self.snippet = snippet
        if experience is None:
            self.experience = 'не указан'
        else:
            self.experience = experience
        if employment is None:
            self.employment = 'не указан'
        else:
            self.employment = employment

    @classmethod
    def validator_pay(cls, pay, json_path):
        """ Валидирует и форматирует данные по зарплате. """
        if pay is None:
            pay_ = 0
            pay_str_ = 'не указана'
        else:
            if pay[0] is None:
                pay_ = 0
                pay_str_ = f'до {pay[1]} {pay[2]}'
            else:
                if pay[2] == 'RUR':
                    pay_ = pay[0]
                else:
                    valuta = converter(json_path, pay[2])
                    pay_ = pay[0] * valuta[1] / valuta[0]
                if pay[1] is not None:
                    pay_str_ = f'От {pay[0]} до {pay[1]} {pay[2]}'
                else:
                    pay_str_ = f'От {pay[0]} {pay[2]}'
        return pay_, pay_str_

    def format_published(self):
        """ Преобразует строковую дату в datetime. """
        return datetime.strptime(self.published[0:-5], '%Y-%m-%dT%H:%M:%S')

    def __gt__(self, other):
        """ Метод сравнения объектов по зарплате. """
        return self.pay > other.pay

    def __str__(self):
        return (f'Id: {self.id_}\nВакансия: {self.vacancy}\n'
                f'Дата публикации: {self.published}\n'
                f'Компания: {self.company}\nURL: {self.url}\n'
                f'Зарплата: {self.pay_str}\nАдрес: {self.address}\n'
                f'Требования: {self.snippet}\nОпыт: {self.experience}\n'
                f'Тип занятости: {self.employment}\n')
