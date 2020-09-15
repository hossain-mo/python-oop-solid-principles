from WeightHolder import WeightHolder
from Car import Car


class TruckXt(Car, WeightHolder):
    def move(self):
        return "move by speed {}".format(self.speed)

    def accelerate(self):
        return "accelerate by speed {} and have gearboxSystem {}".format(self.speed, self.gearboxSystem)

    def park(self):
        return True

    def leftCargo(self):
        return "Hold The Weight"
