import requests


class ApiHH:
    def __init__(self, employer_id):
        self.url = 'https://api.hh.ru/employers'
        self.employer_id = employer_id

    def get_vacancy_api(self):
        response = requests.get(f'https://api.hh.ru/vacancies?employer_id={self.employer_id}&per_page=100')
        data_vacancy = response.json()['items']
        return data_vacancy
