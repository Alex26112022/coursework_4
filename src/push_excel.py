import openpyxl

from config import vacancies_excel
from src.vacancy import Vacancy


class PushExcel:
    """ Класс взаимодействия с Excel документом. """

    def __init__(self, list_vacancies: list[Vacancy]):
        self.list_vacancies = list_vacancies

    def push_excel(self):
        """ Создает Excel-документ и записывает в него вакансии. """
        book = openpyxl.Workbook()
        book.remove(book.active)
        page = book.create_sheet('Вакансии')
        row = 1
        column = 1

        for item in self.list_vacancies:
            page.cell(row=row, column=column, value=item.id_)
            page.cell(row=row, column=column + 1, value=item.vacancy)
            page.cell(row=row, column=column + 2, value=item.url)
            page.cell(row=row, column=column + 3, value=item.pay_str)
            page.cell(row=row, column=column + 4, value=item.published)
            page.cell(row=row, column=column + 5, value=item.address)
            page.cell(row=row, column=column + 6, value=item.company)
            page.cell(row=row, column=column + 7, value=item.schedule)
            page.cell(row=row, column=column + 8, value=item.employment)
            page.cell(row=row, column=column + 9, value=item.experience)
            page.cell(row=row, column=column + 10, value=item.snippet)
            row += 1

        book.save(vacancies_excel)
        print('Данные успешно сформированы в Excel-документ в папке "data"!')
