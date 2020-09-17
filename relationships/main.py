from teacher import Teacher
from htmlprinter import HTMLPrinter
from plaintextprinter import PlainTextPrinter
from student import Student
from scienceteacher import ScienceTeacher
from mathteacher import MathTeacher
from project import Project
from developer import Developer
from room import Room
from house import House
import datetime

# association relationship cause if any object destroyed another object can complete its life cycle
# 1) one unidirectional association
htmlPrinter = HTMLPrinter("HTML Message")
plainTextPrinter = PlainTextPrinter("Plain Text Printer Message")
mohamed = Teacher("Mohammed")
print(mohamed.sayWelcome(htmlPrinter))
print(mohamed.sayWelcome(plainTextPrinter))
# 1) one bidirectional association
hossain = Student("Hossain", "Do Your HomeWork")
alaa = MathTeacher("Alaa")
ebrahim = ScienceTeacher("Ebrahim")
print(hossain.assignATempTeacher(alaa))
print(hossain.assignATempTeacher(ebrahim))
print(alaa.evaluateStudentHomeWork(hossain))
print(ebrahim.evaluateStudentHomeWork(hossain))
# aggregation there is ownership relation between project and developers but when project is finished there is
# developers
ahmed = Developer("Ahmed")
ali = Developer("Ali")
abdullah = Developer("Abdullah")
csProject = Project("OS", datetime.datetime.now(), [ahmed, ali, abdullah])
print(csProject.showDetails())

# composition there is ownership but when we destroy the owner class the owned classes has not meaning
room1 = Room("Red", 250, "first")
room2 = Room("White", 350, "second")
room3 = Room("Blue", 280, "third")
house = House([room1, room2, room3])
print(house.getDetails())
