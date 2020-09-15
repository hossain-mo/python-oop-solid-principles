from Car import Car
class Mercedes (Car):
    def move(self):
        return "move by speed {}".format(self.speed * 2)

    def accelerate(self):
        return "accelerate by speed {} and have gearboxSystem {}".format(self.speed * 2, self.gearboxSystem)

    def park(self):
        print("Mercedes was parked")
        return True