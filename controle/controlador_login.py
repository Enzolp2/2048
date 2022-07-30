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
                self.__controlador_sistema.iniciar_game(typed["usuario"])

    def criar_conta(self):
        opcao = self.__tela_login.tela_opcoes_usuario()
        lista_op = {1: self.incluir_usuario, 2: self.alterar_usuario,
                    3: self.listar_usuario, 4: self.excluir_usuario,
                    0: self.abre_tela_inicial}
        while True:
            lista_op[opcao]()

    def incluir_usuario(self):
        typed = self.__tela_login.tela_login()
        if typed["usuario"] in self.__logins:
            print('Usuário já cadastrado.')
            self.criar_conta()
        else:
            login = Login(typed["usuario"], typed["senha"])
            self.__logins[login.usuario] = login.senha
            print("Usuário Cadastrado!")
            self.abre_tela_inicial()

    def alterar_usuario(self):
        usuario = self.__tela_login.pede_usuario()
        if usuario in self.__logins:
            print("--- ALTERAR USUÁRIO ---")
            novo_usuario = str(input("Novo usuario: "))
            try:
                self.__logins[novo_usuario] = self.__logins.pop(usuario)
                print("Usuário alterado com sucesso.")
                print(f"Novo usuário: {novo_usuario}")
                self.abre_tela_inicial()
            except Exception:
                print("Usuário não encontrado.")
                self.criar_conta()
        else:
            print("Usuário não encontrado.")
            self.criar_conta()

    def listar_usuario(self):
        print("------ USUÁRIOS ------")
        for login in self.__logins:
            print(f'- {login}')
        self.abre_tela_inicial()


    def excluir_usuario(self):
        usuario = self.__tela_login.tela_login()
        if usuario["usuario"] in self.__logins:
            if usuario["senha"] == self.__logins[usuario["usuario"]]:
                self.__logins.pop(usuario["usuario"])
                print("Usuário excluído.")
                self.abre_tela_inicial()
        else:
            print('Usuário não encontrado.')
            self.criar_conta()

    def abre_tela_inicial(self):
        opcao = self.__tela_login.tela_opcoes_login()
        lista_op = {1: self.realiza_login, 2: self.criar_conta,
                    0: self.__controlador_sistema.encerra_sistema}
        while True:
            lista_op[opcao]()

