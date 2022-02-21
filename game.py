from jogador import jogador

class game:

    def __init__(self):
        self.jogadorUm = jogador(True)
        self.jogadorDois = jogador(False)
        print('Instanciando jogo')