

class TelaGame:
    def __init__(self):
        pass

    def menu_inicial(self):
        print("-------- 2048 Game ---------")
        print("1 -> Iniciar Game")
        print("2 -> Ranking")
        print("0 -> Logout")
        opcao = int(input())
        return opcao
