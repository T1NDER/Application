import unittest

from __init__ import calculate_salary

class TestCalculateSalary(unittest.TestCase):

    # Тестирование функции calculate_salary из модуля salary

    def test_calculate_salary_on_the_payroll(self):
        """" Тестируем корректный расчёт зарплаты """

        employees = [
            {"id": "1", "name": "Пётр", "position": "Разработчик", "year_of_work": "3"},
            {"id": "2", "name": "Анастасия", "position": "Маркетолог", "year_of_work": "4"},
            {"id": "3", "name": "Валерия", "position": "Веб-Дизайнер", "year_of_work": "3"},
            {"id": "4", "name": "Олег", "position": "Разработчик", "year_of_work": "5"},
        ]

        salary_rates = {
            'Разработчик': 50000,
            'Маркетолог': 60000,
            'Веб-Дизайнер': 40000,
        }

        expected_salaries = {
            0: 200000,
            1: 300000,
            2: 120000
        }

        calculate_salaries = calculate_salary(employees, salary_rates)
        self.assertEquals(calculate_salaries, expected_salaries)

    def test_calculate_salary_with_valid_data(self):
        """ Тест с действительными данными о сотрудниках и ставках заработной платы"""

        employees = [
            {"position": "Software Engineer", "year_of_work": "5"},
            {"position": "Data Analyst", "year_of_work": "2"},
            {"position": "Project Manager", "year_of_work": "10"}
        ]
        salary_rates = {
            "Software Engineer": 1000,
            "Data Analyst": 800,
            "Project Manager": 1200
        }
        expected_salaries = {0: 5000, 1: 1600, 2: 12000}
        self.assertEqual(calculate_salary(employees, salary_rates), expected_salaries)


if __name__ == '__main__':
    unittest.main()