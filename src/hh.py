import json

import requests


class HH:
    """Класс для работы с API HeadHunter"""
    def __init__(self, employer_id):
        self.data_vacancy = None
        self.url = 'https://api.hh.ru/employers'
        self.employer_id = employer_id

    def get_vacancy_api(self):
        response = requests.get(f'https://api.hh.ru/vacancies?employer_id={self.employer_id}&per_page=50')
        self.data_vacancy = response.json()['items']

class VacancyHH:
    """Класс для работы с вакансиями"""

    def __init__(self, name_vacancy: str, link_vacancy: str, salary: int, short_description: str, requirements: str):
        self.name_vacancy = name_vacancy
        self.link_vacancy = link_vacancy
        self.salary = salary if salary else 0
        self.short_description = short_description if short_description else 'Краткое описание не указаны'
        self.requirements = requirements if requirements else 'Требования не указаны'

    def __lt__(self, other):
        """Метод стравнения"""
        return self.salary < other.salary

    def __repr__(self):
        return f"Salary {self.salary}"

    def to_dict(self):
        """Метод возвращает словарь который можно добавить"""
        data_vacancy = {
            'name_vacancy': self.name_vacancy,
            'link_vacancy': self.link_vacancy,
            'salary': self.salary,
            'short_description': self.short_description,
            'requirements': self.requirements}
        return data_vacancy

class JsonConnector:
    def __init__(self):
        self.data_vacancy = []

    def add_vacancy(self, job):
        """Метод добавления"""
        self.data_vacancy.append(job)

    def save_to_file_json(self, data_vacancy):
        """Методо сохранения файла"""
        with open('all_vacancies.json', 'w', encoding="utf-8") as file:
            json.dump(data_vacancy, file, ensure_ascii=False, indent=4)

    def load_file(self):
        """Метод открытия файла"""
        with open('all_vacancies.json', 'r', encoding="utf-8") as file:
            self.data_vacancy = json.load(file)
            return self.data_vacancy
