class Vacancy:
    """ Класс экземпляра вакансии. """
    def __init__(self, id_, vacancy, company, url, pay, address,
                 snippet, experience, employment):
        self.id_ = id_
        self.vacancy = vacancy
        self.company = company
        self.url = url
        self. pay = pay
        self.address = address
        self.snippet = snippet
        self.experience = experience
        self.employment = employment

    def __str__(self):
        return (f'Id: {self.id_}\nВакансия: {self.vacancy}\n'
                f'Компания: {self.company}\nURL: {self.url}\n'
                f'Зарплата: {self. pay}\nАдрес: {self.address}\n'
                f'Требования: {self.snippet}\nОпыт: {self.experience}\n'
                f'Тип занятости: {self.employment}\n')
