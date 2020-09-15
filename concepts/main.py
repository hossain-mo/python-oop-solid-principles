# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from MicroWave import MicroWave
from BMW import Bmw
from Mercedes import Mercedes
from Order import Order
from TruckXt import TruckXt
from CarDashboard import CarDashboard
from HTTPClinet import HTTPClient
from TCPClient import TCPClient
from Employee import Employee
from Salary import Salary
from OrganiztionSalary import OrganizationSalary

# Press the green button in the gutter to run the script.

# apply abstraction how to use not how to work
microWave = MicroWave(90, "DE", 30)
if microWave.turnOn():
    print(microWave.deFreeze())
if not microWave.turnOff():
    print(microWave.deFreeze())
firstOrder = Order("maadi", "Helwan", "2KG")
secondOrder = Order("zamalek", "sheaton", "12KG")
bmw = Bmw(200, 4, "red", "BM Gear")
mercedes = Mercedes(290, 6, "yellow", "Mer Gear")
truck = TruckXt(260, 5, "blue", "TruckXt Gear")
print(firstOrder.deliver(bmw))
print(secondOrder.deliver(mercedes))
print(secondOrder.deliver(truck))

# Encapsulation

print(bmw.readCarInfo())
mercedesDashboard = CarDashboard(150, 120, 87)
mercedes.installDashboard(mercedesDashboard)
print(mercedes.readCarInfo())

# Inheritance

httpClient = HTTPClient("192.168.0.1", 50)
print(httpClient.connect())
print(httpClient.welcomeAfterConnection())
print(httpClient.call("www.google.com"))
print(httpClient.terminate())

tcpClient = TCPClient("192.168.0.12", 40, 154)
print(tcpClient.connect())
print(tcpClient.call("www.python.com"))
print(tcpClient.terminate())

# Polymorphism
# 1) Dynamic Polymorphism
doctorSalary = Salary(5000, .10, 500, 12, 15)
doctor = Employee(20, "ahmed", "maadi", doctorSalary)
print(doctor.getSalary().calculate())
engineerSalary = OrganizationSalary(10000, .15, 500, 12, 15, 2000)
engineer = Employee(23, "hossain", "maadi", engineerSalary)
print(engineer.getSalary().calculate())
# there is no static polymorphism because there is no method overloading in python
