from abc import abstractmethod
from CarDashboard  import CarDashboard

class Car:
    __turnedOn = False
    __dashboard = False

    def __init__(self, speed, numOfDoors, color, gearboxSystem):
        self.speed = speed
        self.numOfDoors = numOfDoors
        self.color = color
        self.gearboxSystem = gearboxSystem

    abstractmethod

    def move(self):
        pass

    def turnOn(self):
        self.turnedOn = True
        return True

    def turnOff(self):
        self.turnedOn = False
        return False

    abstractmethod

    def accelerate(self):
        pass

    abstractmethod

    def park(self):
        pass

    def installDashboard(self, CarDashboard):
        self.__dashboard = CarDashboard

    def readCarInfo(self):
        if self.__dashboard:
            return "The speed is {} more info ...".format(self.speed) + self.__dashboard.read()
        else:
            return "The speed is {}".format(self.speed)