# Функция для расчета зарплаты

def calculate_salary(employees, salary_rates):

    calculated_salaries = {}

    for employee_id, employee in enumerate(employees):
        position = employee['position']

        if position in salary_rates:
            salary_rate = salary_rates[position]

            salary = salary_rate * int(employee['year_of_work'])

            calculated_salaries[employee_id] = salary
        else:
            print('Ошибка')

    return calculated_salaries


