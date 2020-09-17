from teacher import Teacher
class MathTeacher(Teacher):
    def __init__(self, name, ):
        super(MathTeacher, self).__init__(name)
    def assignAHomeWork(self):
        return "Calculate the sum of 10 and 12"