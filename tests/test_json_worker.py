from config import vacancies_json_test
from src.json_worker import VacancyJson

new_list = [
    {
        "id": "96034351",
        "name": "Junior Python",
        "salary": {
            "from": 50000,
            "to": 100000,
            "currency": "RUR"
        },
        "employer": {"name": "Yakov Lushkov Neuro-Agency"},
        "address": {"city": "Москва"},
        "snippet": {"requirement": "Знание Python на базовом уровне"},
        "experience": {"name": "нет опыта"},
        "employment": {"name": "полный рабочий день"},
        "alternate_url": "https://hh.ru/vacancy/96034351",
        "published_at": "2024-04-04T13:09:44+0300"
    },
    {
        "id": "96034352",
        "name": "Python developer",
        "salary": {
            "from": 100000,
            "to": 200000,
            "currency": "RUR"
        },
        "employer": {"name": "Skypro"},
        "address": {"city": "Санкт-Петербург"},
        "snippet": {"requirement": "Знание Django"},
        "experience": {"name": "от 1 до 3 лет"},
        "employment": {"name": "удаленная работа"},
        "alternate_url": "https://hh.ru/vacancy/94450348",
        "published_at": "2024-03-04T13:09:44+0300"
    }
]

add_list = [{"id": "11", "name": "test1"}, {"id": "12", "name": "test2"}]


def test_json_worker():
    """ Тестирует класс работы с файлом json. """
    new_vac = VacancyJson(new_list, vacancies_json_test)
    new_vac.load_json()
    new_vac.read_json()
    new_vac.add_json(add_list)
    new_vac.del_json("id", "11")
