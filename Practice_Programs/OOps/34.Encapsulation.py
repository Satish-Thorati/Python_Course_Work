#34. Secure Salary Data

class Employee:
    def __init__(self, salary):
        self.__salary = salary

def get_salary(self):
    return self.__salary

emp = Employee(40000)
print(emp.get_salary())