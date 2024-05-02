from src.api import ApiHH
from src.db_manager import DBManager
from src.hh import VacancyHH
from src.utils import save_to_json


def main():
    base_employer = [
        1740,  # Яндекс,
        78638,  # Тинькофф
        3529,  # Сбер
        9352463,  # X5
        1057,  # Касперский
        4781293,  # Genius Group
        407,  # Гарант
        1351014,  # Симфософт
        3776,  # МТС
        3148  # Ситилинк
    ]
    data_vacancy = []
    for employer in base_employer:
        api_hh = ApiHH(employer)
        vacancy_data = api_hh.get_vacancy_api()
        vacancy_list = []
        for vacancy in vacancy_data:
            vacancy_hh = VacancyHH(vacancy['name'], vacancy['salary'], vacancy['snippet']['requirement'],
                                   vacancy['snippet']['responsibility'],
                                   vacancy['apply_alternate_url'], vacancy['id'], employer)
            vacancy_list.append(vacancy_hh)
        data_vacancy.extend(vacancy_list)
    data_vacancy_dict = [vacancy.to_dict() for vacancy in data_vacancy]
    save_to_json(data_vacancy_dict)
    db = DBManager('api_hh', 'postgres', '449558', 'localhost')
    db.clear_db()
    db.insert_into_db(data_vacancy_dict)

    while True:
        print("1. Получить список всех компаний и количество вакансий у каждой компании")
        print("2. Получить список всех вакансий")
        print("3. Получить среднюю зарплату по вакансиям")
        print("4. Получить список всех вакансий, у которых зарплата выше средней по всем вакансиям")
        print("5. Получить список всех вакансий, в названии которых содержатся переданные слова")
        print("6. Выход")
        choice = input("Введите номер вашего выбора: ")
        if choice == '1':
            print(db.get_companies_and_vacancies_count())
        elif choice == '2':
            print(db.get_all_vacancies())
        elif choice == '3':
            print(db.get_avg_salary())
        elif choice == '4':
            print(db.get_vacancies_with_higher_salary())
        elif choice == '5':
            keyword = input("Введите ключевое слово: ")
            print(db.get_vacancies_with_keyword(keyword))
        elif choice == '6':
            break
        else:
            print("Неверный ввод. Пожалуйста, введите номер от 1 до 6.")


if __name__ == "__main__":
    main()
