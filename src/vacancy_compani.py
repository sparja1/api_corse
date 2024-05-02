class VacancyHH:
    def __init__(self, name_vacancy: str, salary: int, short_description: str,
                 requirements: str, apply_alternate_url: str, id_vacancy: int, id_company: int):
        self.name_vacancy = name_vacancy
        if salary:
            self.salary = salary['from']
        elif salary:
            self.salary = salary['to']
        else:
            self.salary = 0
        self.short_description = short_description if short_description else 'Краткое описание не указано'
        self.requirements = requirements if requirements else 'Требования не указаны'
        self.apply_alternate_url = apply_alternate_url
        self.id_vacancy = id_vacancy
        self.id_company = id_company

    def to_dict(self):
        data_vacancy = {
            'id_company': self.id_company,
            'id_vacancy': self.id_vacancy,
            'name_vacancy': self.name_vacancy,
            'salary': self.salary,
            'short_description': self.short_description,
            'requirements': self.requirements,
            'apply_alternate_url': self.apply_alternate_url}
        return data_vacancy