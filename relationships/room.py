class Room:
    def __init__(self, color, size, name):
        self._color = color
        self._size = size
        self._name = name

    def getInfo(self):
        return "{} room size is {} and color is {}".format(self._name, self._size, self._color)
