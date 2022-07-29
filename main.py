from controle.controlador_game import ControladorGame
import hashlib
import getpass


#if __name__ == "__main__":
   # ControladorGame().inicializar_game()


dict = {"enzo": 22, "joice": 26, "gessica": 30}

teste = {"usuario": "enzo", "password": 22}

print(dict[teste["usuario"]])
if dict[teste["usuario"]] == teste["password"]:
    print('Login Efetuado!')
