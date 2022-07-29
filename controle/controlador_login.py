from limite.tela_login import TelaLogin
from entidade.login import Login

class ControladorLogin:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__logins = {}
        self.__tela_login = TelaLogin()

    def realiza_login(self):
        typed = self.__tela_login.tela_login()
        if typed["usuario"] in self.__logins:
            if self.__logins[typed["usuario"]] == typed["senha"]:
                self.__controlador_sistema.iniciar_game()

    def criar_conta(self):
        opcao = self.__tela_login.tela_opcoes_usuario()
        lista_op = {1: self.incluir_usuario(), 2: self.alterar_usuario(),
                    3: self.listar_usuario(), 4: self.excluir_usuario(),
                    0: self.abre_tela_inicial()}
        while True:
            lista_op[opcao]

    def incluir_usuario(self):
        typed = self.__tela_login.tela_login()
        login = Login(typed["usuario"], typed["senha"])
        self.__logins[typed["usuario"]] = typed["senha"]

    def alterar_usuario(self):
        pass

    def listar_usuario(self):
        pass

    def excluir_usuario(self):
        pass

    def abre_tela_inicial(self):
        opcao = self.__tela_login.tela_opcoes_login()
        lista_op = {1: self.realiza_login(), 2: self.criar_conta(),
                    0: self.encerra_sistema()}
        while True:
            lista_op[opcao]

    def encerra_sistema(self):
        exit(0)

