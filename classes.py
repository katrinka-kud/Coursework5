import requests

from config import EMPLOYERS_URL, VACANCIES_URL


class Employer:

    def __init__(self, employer_id: str, employer_name: str, employer_vacancies: int, employer_url: str):
        self.employer_id = employer_id
        self.employer_name = employer_name
        self.employer_vacancies = employer_vacancies
        self.employer_url = employer_url

    @classmethod
    def initiate_from_hh(cls, em_ids: list):
        employers_list = []
        for em_id in em_ids:
            response = requests.get(url=f"{EMPLOYERS_URL}{em_id}").json()
            employer_id = response['id']
            employer_name = response['name']
            employer_vacancies = response['open_vacancies']
            employer_url = response['alternate_url']
            employer = Employer(employer_id, employer_name, employer_vacancies, employer_url)
            employers_list.append(employer)
        return employers_list


class Vacancy:

    def __init__(self,
                 employer_id: str,
                 vacancy_id: int,
                 vacancy_name: str,
                 salary_from: int,
                 salary_to: int,
                 currency: str,
                 vacancy_url: str):
        self.employer_id = employer_id
        self.vacancy_id = vacancy_id
        self.vacancy_name = vacancy_name
        self.salary_from = self.validate_salary_from(salary_from)
        self.salary_to = self.validate_salary_to(salary_from, salary_to)
        self.currency = currency
        self.vacancy_url = vacancy_url

    @classmethod
    def initiate_from_hh(cls, employer_id: str):
        params = {
            'page': 0,
            'per_page': 100,
            'only_with_salary': True,
            'employer_id': employer_id
        }
        vacancies_list = []
        employer_vacancies = requests.get(url=VACANCIES_URL, params=params).json()
        for unit in employer_vacancies['items']:
            emp_id = employer_id
            vacancy_id = unit['id']
            vacancy_name = unit['name']
            salary_from = unit['salary']['from']
            salary_to = unit['salary']['to']
            currency = unit['salary']['currency']
            vacancy_url = unit['alternate_url']
            vacancy = Vacancy(emp_id, vacancy_id, vacancy_name, salary_from, salary_to, currency, vacancy_url)
            vacancies_list.append(vacancy)
        return vacancies_list

    @staticmethod
    def validate_salary_from(salary):
        if not salary:
            return 0
        return salary

    @staticmethod
    def validate_salary_to(salary_from, salary_to):
        if not salary_to:
            salary_to = salary_from
        return salary_to
