import json

from config import vacancies_json


with open(vacancies_json, encoding='utf-8') as file:
    f = json.load(file)
    for vacancy in f:
        # print(vacancy, '\n')
        vacancy_id = vacancy.get("id")
        vacancy_title = vacancy.get("name")
        vacancy_url = vacancy.get("alternate_url")
        company_name = vacancy.get("employer", {}).get("name")
        salary = vacancy.get("salary", {})
        if salary is not None:
            salary = salary.get("from"), salary.get('to'), salary.get("currency")
        address = vacancy.get("address")
        if address is not None:
            address = address.get("city")
        snippet = vacancy.get("snippet", {})
        if snippet is not None:
            snippet = snippet.get("requirement")
            if snippet is not None:
                snippet = snippet.replace('<highlighttext>', '')
                snippet = snippet.replace('</highlighttext>', '')
        experience = vacancy.get("experience", {})
        if experience is not None:
            experience = experience.get("name")
        employment = vacancy.get("employment", {})
        if employment is not None:
            employment = employment.get("name")

        print(
            f"ID: {vacancy_id}\nВакансия: {vacancy_title}\nКомпания: {company_name}\n"
            f"URL: {vacancy_url}\nЗарплата: {salary}\nАдрес: {address}\n"
            f"Требования: {snippet}\nОпыт: {experience}\n"
            f"Тип занятости: {employment}\n")
