class Salary:
    def __init__(self, salary, tax, overtime, absent, absentRate):
        self._salary = salary
        self._tax = tax
        self._overtime = overtime
        self._absent = absent
        self._absentRate = absentRate

    def calculate(self):
        return self._salary - (self._salary * self._tax)