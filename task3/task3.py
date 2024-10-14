import json
import sys

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def create_value_dict(values):
    return {item['id']: item['value'] for item in values}

def fill_values(node, value_dict):
    if 'id' in node:
        node['value'] = value_dict.get(node['id'], '')
    
    if 'values' in node:
        for child in node['values']:
            fill_values(child, value_dict)

def process_tests(tests, value_dict):
    for test in tests:
        fill_values(test, value_dict)

def main(values_path, tests_path, report_path):
    # Загрузка данных
    values_data = load_json(values_path)
    tests_data = load_json(tests_path)

    # Создание словаря значений
    value_dict = create_value_dict(values_data['values'])

    # Обработка тестов
    process_tests(tests_data['tests'], value_dict)

    # Сохранение отчета
    save_json(tests_data, report_path)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Использование: python task3.py values.json tests.json report.json")
        sys.exit(1)

    values_path = sys.argv[1]
    tests_path = sys.argv[2]
    report_path = sys.argv[3]

    main(values_path, tests_path, report_path)