<<<<<<< HEAD


class TelaGame:
    def menu_inicial(self):
        print("-------- 2048 Game ---------")
        print("1 -> Iniciar Game")
        print("2 -> Ranking")
        print("0 -> Logout")

        return int(input("Escolha a opção: "))

    def pegar_entrada(self):
        return str(input("UP    ->   W\n"
                         "DOWN  ->   S\n"
                         "LEFT  ->   A\n"
                         "RIGHT ->   D\n"
                         "SAIR  ->   0\n"
                         "->")).upper()
=======


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
>>>>>>> 8a18778d75953f0dcd8d7eabf1b2d715bf9bec6b
