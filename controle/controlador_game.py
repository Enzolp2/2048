from limite.tela_game import TelaGame
from entidade.game import Game
import random

class ControladorGame:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__usuario = None
        self.__game = Game()
        self.__tela_game = TelaGame()
        self.__matriz = []

    def inicializar_game(self, usuario):
        self.__usuario = usuario
        opcao = self.__tela_game.menu_inicial()
        lista_op = {1: self.game, 2: self.ranking,
                    0: self.__controlador_sistema.iniciar}
        while True:
            lista_op[opcao]()

    def get_current_status(self):
        for i in range(4):
            for j in range(4):
                if self.__matriz[i][j] == 2048:
                    self.__controlador_sistema.encerra_sistema()
                    return "PARABÉNS VOCÊ VENCEU!"

        for i in range(4):
            for j in range(4):
                if self.__matriz[i][j] == 0:
                    return "O JOGO AINDA NÃO ACABOU"

        for i in range(3):
            for j in range(3):
                if (self.__matriz[i][j] == self.__matriz[i + 1][j] or self.__matriz[i][j] == self.__matriz[i][j + 1]):
                    return 'O JOGO AINDA NÃO ACABOU'

        for j in range(3):
            if (self.__matriz[3][j] == self.__matriz[3][j + 1]):
                return 'O JOGO AINDA NÃO ACABOU'

        for i in range(3):
            if (self.__matriz[i][3] == self.__matriz[i + 1][3]):
                return 'O JOGO AINDA NÃO ACABOU'

        return 'VOCÊ PERDEU =('

    def game(self):
        self.__game.running = True
        self.inicializa_matriz()
        lista_op = {"W": self.move_up, "S": self.move_down,
                    "A": self.move_left, "D": self.move_right,
                    "0": self.__controlador_sistema.encerra_sistema}
        while self.__game.running:
            self.mostrar_matriz()
            opcao = self.__tela_game.pegar_entrada()
            lista_op[opcao]()
            status = self.get_current_status()
            print(status)
            if status == 'VOCÊ PERDEU =(':
                self.mostrar_matriz()
                self.__controlador_sistema.encerra_sistema()
            self.add_two()

    def inicializa_matriz(self):
        for i in range(4):
            self.__matriz.append([0] * 4)
        for i in range(2):
            k = random.randint(0, 3)
            j = random.randint(0, 3)
            self.__matriz[k][j] = 2

    def add_two(self):
        k = random.randint(0, 3)
        j = random.randint(0, 3)

        while self.__matriz[k][j] != 0:
            k = random.randint(0, 3)
            j = random.randint(0, 3)

        self.__matriz[k][j] = 2

    def inverter(self):
        nova_matriz = []
        for i in range(4):
            nova_matriz.append([])
            for j in range(4):
                nova_matriz[i].append(self.__matriz[i][3-j])
        self.__matriz = nova_matriz

    def transpor(self):
        nova_matriz = []
        for i in range(4):
            nova_matriz.append([])
            for j in range(4):
                nova_matriz[i].append(self.__matriz[j][i])

        self.__matriz = nova_matriz

    def compress(self):
        nova_matriz = []
        changed = False
        for i in range(4):
            nova_matriz.append([0] * 4)

        for i in range(4):
            pos = 0
            for j in range(4):
                if self.__matriz[i][j] != 0:
                    nova_matriz[i][pos] = self.__matriz[i][j]
                    if j != pos:
                        changed = True
                    pos += 1

        self.__matriz = nova_matriz
        return changed

    def merge(self):
        changed = False
        for i in range(4):
            for j in range(3):
                if (self.__matriz[i][j] == self.__matriz[i][j+1]) and (self.__matriz[i][j] != 0):
                    self.__matriz[i][j] = self.__matriz[i][j] * 2
                    self.__matriz[i][j + 1] = 0
                    changed = True

        return changed

    def move_left(self):
        changed1 = self.compress()
        changed2 = self.merge()
        changed = changed1 or changed2
        self.compress()

        return changed

    def move_right(self):
        self.inverter()
        changed = self.move_left()
        self.inverter()

        return changed

    def move_up(self):
        self.transpor()
        changed = self.move_left()
        self.transpor()

        return changed

    def move_down(self):
        self.transpor()
        changed = self.move_right()
        self.transpor()

        return changed

    def mostrar_matriz(self):
        for i in range(4):
            print(self.__matriz[i])

    def ranking(self):
        pass
