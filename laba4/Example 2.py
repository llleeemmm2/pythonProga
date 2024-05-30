'''Добавление ещё трёх сотрудников.'''

from mainClass import factory
from mainClass import Employee, JobGrades, JobHistory, Job, Location, Region

e1 = Employee(employee_id = "1337", first_name = "Ковалевский", last_name = 'Максим',
              email = "abc123456789101112131415", phone_number = "12354678",
              hire_date = "2004-06-19", job_id = "IT_PROG", salary = "68000",
              commission_pct = "0.2", manager_id = "124", department_id = "90")

e2 = Employee(employee_id = "209", first_name = "Вадимыч", last_name = 'Дробовик',
              email = "vadyabruh", phone_number = "987654321",
              hire_date = "2004-01-14", job_id = "SA_REP", salary = "70500",
              commission_pct = None, manager_id = "100", department_id = "50")

e3 = Employee(employee_id = "123", first_name = "Пабло", last_name = "Веселков",
              email = "veselkov111", phone_number = "789.789.7890",
              hire_date = "2004-04-01", job_id = "IT_PROG", salary = "85000",
              commission_pct = "0.05", manager_id = "124", department_id = "110")

print(e1)
print(e2)
print(e3)

session = factory()

session.add(e1)
session.add(e2)
session.add(e3)

session.commit()