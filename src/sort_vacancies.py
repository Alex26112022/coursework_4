from src.list_vacancies import ListVacancies


class SortVacancies:
    """ Класс сортировки и фильтрации вакансий. """
    def __init__(self, json_path):
        new_list = ListVacancies(json_path)
        new_list.generate_vacancies()
        self.all_vacancies = new_list.get_all_vacancies()

    def sort_pay(self):
        """ Сортирует вакансии по зарплате """
        self.all_vacancies.sort(reverse=True)

    def sort_published(self):
        """ Сортирует вакансии по дате публикации. """
        self.all_vacancies.sort(key=lambda x: x.format_published(), reverse=True)

    def filter_address(self, expected_address: str):
        """ Фильтрует список по названию города. """
        filter_list = []
        for vacancy in self.all_vacancies:
            if vacancy.address.lower().strip() == expected_address.lower().strip():
                filter_list.append(vacancy)
        self.all_vacancies = filter_list

    def filter_experience(self, expected_experience):
        """ Фильтрует список по опыту работы. """
        filter_list = []
        for vacancy in self.all_vacancies:
            if vacancy.experience == expected_experience:
                filter_list.append(vacancy)
        self.all_vacancies = filter_list

    def filter_employment(self, expected_employment):
        """ Фильтрует список по типу занятости. """
        filter_list = []
        for vacancy in self.all_vacancies:
            if vacancy.employment == expected_employment:
                filter_list.append(vacancy)
        self.all_vacancies = filter_list

    def filter_snippet(self, expected_snippet: str):
        """ Фильтрует список по требуемым навыкам. """
        filter_list = []
        for vacancy in self.all_vacancies:
            if expected_snippet.lower() in vacancy.snippet.lower():
                filter_list.append(vacancy)
        self.all_vacancies = filter_list

    def filter_pay(self, pay_min_=0, pay_max_=9999999):
        """ Фильтрует список по зарплате. """
        filter_list = []
        for vacancy in self.all_vacancies:
            if (pay_max_ >= vacancy.pay_min >= pay_min_ and vacancy.pay_max <=
                    pay_max_):
                filter_list.append(vacancy)
        self.all_vacancies = filter_list

    def get_sort_vacancies(self):
        """ Возвращает отсортированный список вакансий. """
        return self.all_vacancies
