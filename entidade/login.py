

class Login:
    def __init__(self, usuario: str, senha: str):
        if isinstance(usuario, str):
            self.__usuario = usuario
        if isinstance(senha, str):
            self.__senha = senha

    @property
    def usuario(self):
        return self.__usuario

    @property
    def senha(self):
        return self.__senha

    @usuario.setter
    def usuario(self, usuario):
        self.__usuario = usuario

    @senha.setter
    def senha(self, senha):
        self.__senha = senha

