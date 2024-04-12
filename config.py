import os

ROOT_DIR = os.path.dirname(__file__)
vacancies_json = os.path.join(ROOT_DIR, 'src', 'vacancies.json')
valuta_json = os.path.join(ROOT_DIR, 'src', 'valuta.json')
valuta_json_test = os.path.join(ROOT_DIR, 'tests', 'valuta_test.json')
vacancies_json_test = os.path.join(ROOT_DIR, 'tests', 'vacancies_test.json')
all_vacancies_json_test = os.path.join(ROOT_DIR, 'tests',
                                       'all_vacancies_test.json')
vacancies_excel = os.path.join(ROOT_DIR, 'data', 'vacancies.xlsx')
