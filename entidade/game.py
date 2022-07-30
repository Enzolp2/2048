

class Game:
    def __init__(self):
        self.__running = False

    @property
    def running(self):
        return self.__running

    @running.setter
    def running(self, running):
        self.__running = running
