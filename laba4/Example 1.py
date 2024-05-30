'''Добавление сотрудника.'''

from mainClass import factory
from mainClass import Employee, JobGrades, JobHistory, Job, Location, Region

e = Employee()
e.employee_id = "228"
e.first_name = "Илья"
e.last_name = "Мирошник"
e.email = "llleeemmm"
e.phone_number = "123456789"
e.hire_date = "2004-22-12"
e.job_id = "IT_PROG"
e.salary = "90000"
e.commission_pct = None
e.manager_id = "124"
e.department_id = "90"

print(e)

session = factory()
session.add(e)
session.commit()
print(e)