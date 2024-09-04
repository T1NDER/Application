from salary import salary
from datetime import date
import emoji


if __name__ == '__main__':

    employees = [

        {"id": "1", "name": "Пётр", "position": "Разработчик", "year_of_work": "3", "salary": "150.000"},
        {"id": "2", "name": "Анастасия", "position": "Маркетолог", "year_of_work": "4", "salary": "120.000"},
        {"id": "3", "name": "Валерия", "position": "Веб-Дизайнер", "year_of_work": "3", "salary": "170.000"},
        {"id": "4", "name": "Олег", "position": "Разработчик", "year_of_work": "5", "salary": "220.000"}

        ]

    salary_rates = {

          "Разработчик": 150,
          "Маркетолог": 100,
          "Веб-Дизайнер": 120

        }



    calculated_salaries = salary.calculate_salary(employees, salary_rates)
    today = date.today()
    print(f'{calculated_salaries}, {today}')


    result = emoji.emojize('Python is :red_heart')
    print(result)

