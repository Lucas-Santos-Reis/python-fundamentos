class Tabuleiro:
    def __init__(self, tamanho=3):
                self.matriz = [[None for coluna in range(tamanho)] for linha in range(tamanho)]
        
    def exibir(self):
        print("+-------" * 3, "+", sep="")
        for linha in range(3):
            print("|       " * 3, "|", sep="")
            for coluna in range(3):
                print("|   " + str(self.matriz[linha][coluna]) + "   ", end="")
            print("|")
            print("|       " * 3, "|", sep="")
            print("+-------" * 3, "+", sep="")

    def validar_posicao(self, linha, coluna):
        try:
            if linha not in range(3) or coluna not in range(3):
                return False
            if self.matriz[linha][coluna] in ('X', 'O'):
                return False
            else:
                return True
        except IndexError:
            return False

    def resetar(self):
        self.matriz = [[None for coluna in range(3)] for linha in range(3)]

    def verificar_vitoria(self, simbolo, tamanho=3):
         # Verifica linhas e colunas

class Jogador:
    def __init__(self, simbolo):
        self.simbolo = simbolo

Responsabilidades:


Realizar uma jogada válida

Você pode ter:

JogadorHumano

JogadorComputador

Classe Jogo / Partida

Responsabilidades:

Controlar o fluxo da partida

Alternar turnos

Atualizar placar

Decidir quando a partida termina