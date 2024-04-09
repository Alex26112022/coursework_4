from src.valuta import converter


class Vacancy:
    """ Класс экземпляра вакансии. """

    def __init__(self, id_, vacancy, published, company, url, pay, address,
                 snippet, experience, employment):
        self.id_ = id_
        self.vacancy = vacancy
        self.published = published
        self.company = company
        self.url = url
        if pay is None:
            self.pay = 0
            self.pay_str = 'не указана'
        else:
            if pay[0] is None:
                self.pay = 0
                self.pay_str = f'до {pay[1]} {pay[2]}'
            else:
                if pay[2] == 'RUR':
                    self.pay = pay[0]
                else:
                    valuta = converter(pay[2])
                    self.pay = pay[0] * valuta[1] / valuta[0]
                if pay[1] is not None:
                    self.pay_str = f'От {pay[0]} до {pay[1]} {pay[2]}'
                else:
                    self.pay_str = f'От {pay[0]} {pay[2]}'
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
