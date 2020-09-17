import random
class Student:
    __homeWorkScore = 60

    def __init__(self, name, homeWork):
        self._name = name
        self._homeWork = homeWork

    def assignATempTeacher(self, Teacher):
        self._homeWork = Teacher.assignAHomeWork()
        return self._homeWork
    def getHomeWorkScore(self):
        return self.__homeWorkScore
    def doHomeWork(self):
        self.__homeWorkScore = random.randint(20, 100)
