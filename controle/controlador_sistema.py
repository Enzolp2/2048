from controle.controlador_login import ControladorLogin
from controle.controlador_game import ControladorGame

class ControladorSistema:
    def __init__(self):
        self.__controlador_login = ControladorLogin(self)
        self.__controlador_game = ControladorGame(self)

    def iniciar_game(self, usuario):
        self.__controlador_game.inicializar_game(usuario)

    def iniciar(self):
        self.__controlador_login.abre_tela_inicial()

    def encerra_sistema(self):
        exit(0)
