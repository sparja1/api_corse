import json


def save_to_json(data_vacancy):
    with open('all_vacancies.json', 'w', encoding="utf-8") as file:
        json.dump(data_vacancy, file, ensure_ascii=False, indent=4)
