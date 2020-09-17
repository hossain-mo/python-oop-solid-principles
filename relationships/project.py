class Project:
    def __init__(self, name, deadLine, Developer):
        self._name = name
        self._deadLine = deadLine
        self._developers = Developer

    def showDetails(self):
       devs = map(lambda dev: dev.getName(),self._developers)
       return "Project Name :{} ,it's deadline :{}, It's Developers :{}".format(self._name, self._deadLine, list(devs))
