

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
