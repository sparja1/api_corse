import psycopg2
from psycopg2 import sql


class DBManager:
    """
    Класс для работы с базой данных
    """
    def __init__(self, dbname, user, password, host):
        self.conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
        self.cursor = self.conn.cursor()

    def clear_db(self):
        """
        Метод очистки таблиц
        """
        self.cursor.execute("DELETE FROM vacancies;")
        self.cursor.execute("DELETE FROM companies;")
        self.conn.commit()

    def get_companies_and_vacancies_count(self):
        """
        :return: Считает количество вакансий одной компании
        """
        self.cursor.execute("SELECT company_id, COUNT(*) FROM vacancies GROUP BY company_id;")
        return self.cursor.fetchall()

    def get_all_vacancies(self):
        """
        :return: Список всех вакансий
        """
        self.cursor.execute("SELECT company_id, name, salary, apply_alternate_url FROM vacancies;")
        return self.cursor.fetchall()

    def get_avg_salary(self):
        """
        :return: Среднюю зарплату по вакансиям
        """
        self.cursor.execute("SELECT AVG(salary) FROM vacancies WHERE salary IS NOT NULL;")
        return self.cursor.fetchone()

    def get_vacancies_with_higher_salary(self):
        """
        :return: Список всех вакансий, у которых зарплата выше средней по всем вакансиям
        """
        avg_salary = self.get_avg_salary()[0]
        self.cursor.execute(sql.SQL("SELECT company_id, name, salary, apply_alternate_url "
                                    "FROM vacancies WHERE salary > %s;"), (avg_salary,))
        return self.cursor.fetchall()

    def get_vacancies_with_keyword(self, keyword):
        """
        :return: Список всех вакансий, в названии которых содержатся переданные слова"
        """
        self.cursor.execute(sql.SQL("SELECT company_id, name, salary, apply_alternate_url "
                                    "FROM vacancies WHERE name LIKE %s;"), ('%' + keyword + '%',))
        return self.cursor.fetchall()

    def insert_into_db(self, data_vacancy_dict):
        """
        :return:
        """
        for vacancy in data_vacancy_dict:
            base_employer = {
                1740: 'Яндекс',
                78638: 'Тинькофф',
                3529: 'Сбер',
                9352463: 'X5',
                1057: 'Касперский',
                4781293: 'Genius Group',
                407: 'Гарант',
                1351014: 'Симфософт',
                3776: 'МТС',
                3148: 'Ситилинк'
            }
            self.cursor.execute(
                """
                INSERT INTO companies (id, name) VALUES (%s, %s)
                ON CONFLICT (id) DO NOTHING;
                """,
                (vacancy['id_company'], base_employer[vacancy['id_company']])
            )
            self.cursor.execute(
                """
                INSERT INTO vacancies (id, name, salary, short_description, requirements, apply_alternate_url, company_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s);
                """,
                (vacancy['id_vacancy'], vacancy['name_vacancy'], vacancy['salary'], vacancy['short_description'],
                 vacancy['requirements'], vacancy['apply_alternate_url'], vacancy['id_company'])
            )
        self.conn.commit()
