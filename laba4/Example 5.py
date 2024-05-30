'''Удаление сотрудника из базы данных по его имени и фамилии'''

from mainClass import factory
from mainClass import Employee

session = factory()

print("Введите фамилию сотрудника:")
surname = input()

print("Введите имя сотрудника:")
name = input()

e = session.query(Employee).filter(Employee.last_name == surname, Employee.first_name == name).first()
session.delete(e)

session.commit()

print("Удаление сотрудника прошло успешно!")



