<<<<<<< HEAD


class Game:
    def __init__(self):
        self.__running = False

    @property
    def running(self):
        return self.__running

    @running.setter
    def running(self, running):
        self.__running = running
=======


class Game:
    def __init__(self):
        self.__matriz = [[0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0]]
        self.__up_key, self.__down_key, self.__left_key, self.__right_key = False, False, False, False
        self.__running = False
>>>>>>> 8a18778d75953f0dcd8d7eabf1b2d715bf9bec6b
