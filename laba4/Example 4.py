'''Изменение данные для какого-то определенного сотрудника'''

from mainClass import factory
from mainClass import Employee

session = factory()

print("Введите фамилию сотрудника:")
surname = input()

print("Сотрудник найден. Введите новые данные!")

e = session.query(Employee).where(Employee.last_name == surname).first()
print("Имя:")
e.first_name = input()
print("Фамилия:")
e.last_name = input()
print("Адрес почты:")
e.email = input()
print("Телефон:")
e.phone_number = input()
print("Дата найма:")
e.hire_date = input()
print("ID работы:")
e.job_id = input()
print("Зарплата:")
e.salary = input()
print("Комиссия:")
e.commission_pct = input()
print("ID менеджера:")
e.manager_id = input()
print("ID отдела:")
e.department_id = input()

print("Вы успешно изменили данные!")

session.commit()