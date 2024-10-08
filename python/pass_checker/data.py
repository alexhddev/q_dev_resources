# class Employee with name, age and salary
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"Employee(name={self.name}, age={self.age}, salary={self.salary})"
    def __repr__(self):
        return self.__str__()

employeeList = []

employeeList.append(Employee("John", 25, 50000))
employeeList.append(Employee("Jane", 30, 60000))
employeeList.append(Employee("Bob", 35, 70000))
employeeList.append(Employee("Alice", 40, 80000))
employeeList.append(Employee("Mike", 45, 90000))
employeeList.append(Employee("Sarah", 50, 100000))
employeeList.append(Employee("Tom", 55, 110000))
employeeList.append(Employee("Emily", 60, 120000))

def get_all_employees_names():
    nameList = []
    for employee in employeeList:
        nameList.append(employee.name)
    return nameList

def get_maximum_salary():
    maxSalary = 0
    for employee in employeeList:
        if employee.salary > maxSalary:
            maxSalary = employee.salary
    return maxSalary

def get_employees_with_salary_greater_than(salary):
    employeeListWithSalaryGreaterThan = []
    for employee in employeeList:
        if employee.salary > salary:
            employeeListWithSalaryGreaterThan.append(employee)
    return employeeListWithSalaryGreaterThan

print(get_employees_with_salary_greater_than(100000))
