from teacher import Teacher
class ScienceTeacher(Teacher):
    def __init__(self,name):
        super(ScienceTeacher, self).__init__(name)

    def assignAHomeWork(self):
        return "Prepare a research on plants"
