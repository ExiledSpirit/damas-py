from jogador import Jogador
from tabuleiro import Tabuleiro

class Game:
    def __init__(self):
        print('Instanciando jogo')
        self.jogadorUm = Jogador(1)
        self.jogadorDois = Jogador(2)
        self.tabuleiro = Tabuleiro()
        self.tabuleiro.validarMovimento(3, 2, 2, 1, self.jogadorUm)
