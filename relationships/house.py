class House:
    def __init__(self, Room):
        self._rooms = Room

    def getDetails(self):
        return "the house contain {}".format(list(map(lambda room: room.getInfo(), self._rooms)))