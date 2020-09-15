from Car import Car


class Bmw(Car):

    def move(self):
        return "move by speed {}".format(self.speed)

    def accelerate(self):
        return "accelerate by speed {} and have gearboxSystem {}".format(self.speed, self.gearboxSystem)

    def park(self):
        return True
