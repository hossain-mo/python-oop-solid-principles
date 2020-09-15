class CarDashboard:

    def __init__(self, oilLevel, fuelLevel, airPressure):
        self.__oilLevel = oilLevel
        self.__fuelLevel = fuelLevel
        self.__airPressure = airPressure

    def read(self):
        return "Fuel: {} Oil: {} Air pressure:{}".format(self.__fuelLevel, self.__oilLevel, self.__airPressure)
