from Car import Car
from WeightHolder import WeightHolder


class Order:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

    # abstraction here not matter which car subclass
    def deliver(self, Car):
        print(Car.turnOn())
        print(Car.move())
        print(Car.accelerate())
        print(Car.park())
        print(Car.turnOff())
        if isinstance(Car, WeightHolder):
            print(Car.leftCargo())
        return "I am moving from {} to {} to deliver a package of {} K.G".format(self.source, self.destination,
                                                                                 self.weight)
