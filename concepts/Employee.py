from Salary import  Salary
class Employee:
    def __init__(self,age, name, address, Salary):
        self._age = age
        self._name = name
        self._address = address
        self._salary = Salary

    def getSalary(self):
        return self._salary
