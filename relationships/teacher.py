from abc import abstractmethod
class Teacher:
    def __init__(self, name):
        self.name = name
# association relation
    def sayWelcome(self, Printer):
        return Printer.welcome()
        abstractmethod
    def assignAHomeWork(self):
        pass
    def evaluateStudentHomeWork(self, Student):
        Student.doHomeWork()
        if Student.getHomeWorkScore() >= 50:
            return "Success"
        return "Failed"