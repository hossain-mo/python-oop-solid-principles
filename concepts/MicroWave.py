class MicroWave :

    status = False

    def __init__(self, temp, program, time):
        self.temp = temp
        self.program = program
        self. time = time
    def deFreeze(self):

        self.__turnOnMicroWaveHeatingSys()
        self.__loadingDefreezingProgram()
        self.__setTimer()
        return "I am de-freezing the food at " + str(self.temp) + "using the program " + self.program

    def __turnOnMicroWaveHeatingSys(self):

        print("Starting on Heating System")

    def __loadingDefreezingProgram(self):

        print("Loading program {}".format(self.program))

    def __setTimer(self):

        print("Setting de-freezing time to {} seconds".format(self.time))

    def turnOn(self):

        self.status = True
        return True

    def turnOff(self):
        self.status = False
        return True
