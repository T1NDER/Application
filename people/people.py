import requests

# Функция возвращающая уже встроенный список сотрудников

def get_employee_list():

    employees = [

        '1', 'Пётр', 'Разработчик', '3', '150.000',
        '2', 'Анастасия', 'Маркетолог' '4', '120.000',
        '3', 'Валерия',  'Веб-Дизайнер', 'year_of_work', '3', '170.000',
        '4', 'Олег', 'Разработчик', '5', '220.000'

    ]

    return employees

# Функция возвращающая уже встроенный словарь сотрудников

def get_employee_dict():

    employees = [

        {'id': '1', 'name': 'Пётр', 'position': 'Разработчик', 'year_of_work': '3', 'salary': '150.000'},
        {'id': '2', 'name': 'Анастасия', 'position': '', 'Маркетолог': '4', 'salary': '120.000'},
        {'id': '3', 'name': 'Валерия', 'position': 'Веб-Дизайнер', 'year_of_work': '3', 'salary': '170.000'},
        {'id': '4', 'name': 'Олег', 'position': 'Разработчик', 'year_of_work': '5', 'salary': '220.000'},
    ]

    return employees

# Функция чтения информации о сотрудниках из файла

def get_employee_file():

    employee = []

    with open('employees.txt', 'r') as file:
        for line in file:
            employee.append(line.strip())

    return employee

# Функция вызывающая информацию о сотрудниках с использованием базы данных

def get_employee_db(conn):

    employee = []

    cur = conn.connect('база_данных')
    cur.cursor()
    cur.execute(
        "SELECT имя FROM сотрудники"
    )

    for row in cur:
        employee.append(row[0])

    return employee

# Функция вызывающая информацию о сотрудниках из API

def get_employee_API(api_url: str) -> list:

    response = requests.get(api_url)
    response.raise_for_status()

    if response.status_code == 200:
        employees = response.json()

    return employees