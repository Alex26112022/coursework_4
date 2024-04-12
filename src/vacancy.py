from config import valuta_json
from src.valuta import converter
from datetime import datetime


class Vacancy:
    """ Класс экземпляра вакансии. """

    def __init__(self, id_, vacancy, published, company, url, pay, address,
                 snippet, experience, employment,
                 schedule, json_path=valuta_json):
        self.id_ = id_
        self.vacancy = vacancy
        self.published = published
        self.company = company
        self.url = url
        self.pay_min, self.pay_max, self.pay_str = self.validator_pay(pay,
                                                                      json_path)
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
        if schedule is None:
            self.schedule = 'не указан'
        else:
            self.schedule = schedule

    @classmethod
    def validator_pay(cls, pay: tuple | None, json_path) -> tuple:
        """ Валидирует и форматирует данные по зарплате. """
        if pay is None:
            pay_min = 0
            pay_max = 0
            pay_str_ = 'не указана'
        else:
            if pay[1] is None:
                pay_max = 0
            else:
                if pay[2] == 'RUR':
                    pay_max = pay[1]
                else:
                    valuta = converter(json_path, pay[2])
                    pay_max = pay[1] * valuta[1] / valuta[0]
            if pay[0] is None:
                pay_min = 0
                pay_str_ = f'до {pay[1]} {pay[2]}'
            else:
                if pay[2] == 'RUR':
                    pay_min = pay[0]
                else:
                    valuta = converter(json_path, pay[2])
                    pay_min = pay[0] * valuta[1] / valuta[0]
                if pay[1] is not None:
                    pay_str_ = f'От {pay[0]} до {pay[1]} {pay[2]}'
                else:
                    pay_str_ = f'От {pay[0]} {pay[2]}'
        return pay_min, pay_max, pay_str_

    def format_published(self) -> datetime:
        """ Преобразует строковую дату в datetime. """
        return datetime.strptime(self.published[0:-5], '%Y-%m-%dT%H:%M:%S')

    def __gt__(self, other) -> bool:
        """ Метод сравнения объектов по минимальной зарплате. """
        return self.pay_min > other.pay_min

    def __str__(self):
        return (f'Id: {self.id_}\nВакансия: {self.vacancy}\n'
                f'Дата публикации: {self.published}\n'
                f'Компания: {self.company}\nURL: {self.url}\n'
                f'Зарплата: {self.pay_str}\nАдрес: {self.address}\n'
                f'Требования: {self.snippet}\nОпыт: {self.experience}\n'
                f'Тип занятости: {self.employment}\n'
                f'График работы: {self.schedule}\n')
