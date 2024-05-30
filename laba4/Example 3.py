'''Поиск нужных сотрудников'''

from mainClass import factory
from mainClass import Employee, JobGrades, JobHistory, Job, Location, Region

session = factory()

'''Например тех, у кого id отдела = 90'''
print("Сотрудники с 90-м id отдела:")
resultOne = session.query(Employee).filter(Employee.department_id == "90")
for i in resultOne:
    print(i)

print("")

'''Или тех, у кого зарплата > 80000'''
print("Сотрудники с большой зарплатой:")
resultTwo = session.query(Employee).filter(Employee.salary > 80000)
for j in resultTwo:
    print(j)

print("")

'''Или тех, чья фамилия начинается на букву *S*'''
print ("Сотрудники, с фамилией на букву S:")
resultThree = session.query(Employee).filter(Employee.last_name.like("S%")).all()
resultThreeFinal = [str(item) for item in resultThree]
resultThreeSplit = [item.split() for item in resultThreeFinal]
print(resultThreeSplit)