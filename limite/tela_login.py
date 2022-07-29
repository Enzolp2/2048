import hashlib
import getpass

class TelaLogin:
    def tela_login(self):
        usuario = str(input("Usuário: "))
        senha = hashlib.sha512(getpass.getpass("Senha: ").encode("utf-8")).hexdigest()
        return {"usuario": usuario, "senha": senha}

    def tela_opcoes_login(self):
        print("-------- Login ---------")
        print("1 -> Login")
        print("2 -> Criar Conta")
        print("0 -> Sair")

        return int(input("Escolha a opção: "))

    def tela_opcoes_usuario(self):
        print("-------- USUÁRIOS ----------")
        print("Escolha a opção: ")
        print("1 - Incluir Usuário")
        print("2 - Alterar Usuário")
        print("3 - Listar Usuários")
        print("4 - Excluir Usuário")
        print("0 - Retornar")

        return int(input("Escolha a opção: "))

    def pede_usuario(self):
        return str(input("Usuário: "))