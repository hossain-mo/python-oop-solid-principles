from Salary import Salary
class OrganizationSalary(Salary):
    def __init__(self, salary, tax, overtime, absent, absentRate, organizationSalary):
        super().__init__(salary, tax, overtime, absent, absentRate)
        self._organizationSalary = organizationSalary

    def calculate(self):
        return self._salary + self._organizationSalary - (self._salary * self._tax)