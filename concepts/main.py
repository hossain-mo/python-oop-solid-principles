# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from MicroWave import MicroWave
from Car import Car
from BMW import Bmw
from Mercedes import Mercedes
from Order import Order
from TruckXt import TruckXt
from CarDashboard import CarDashboard
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


#Encapsulation

print(bmw.readCarInfo())
mercedesDashboard = CarDashboard(150, 120, 87)
mercedes.installDashboard(mercedesDashboard)
print(mercedes.readCarInfo())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
