

class Game:
    def __init__(self):
        self.__matriz = [[0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0]]
        self.__up_key, self.__down_key, self.__left_key, self.__right_key = False, False, False, False
        self.__running = False
