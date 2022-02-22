class Tabuleiro:
    def __init__(self):
        self.casas = self.inicializarTabuleiro()
        self.inicializarTabuleiro()
        self.printarTabuleiro()

    def inicializarTabuleiro(self):
        return [
            [2, 0, 2, 0, 2, 0, 2, 0],
            [0, 2, 0, 2, 0, 2, 0, 2],
            [2, 0, 2, 0, 2, 0, 2, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
        ]

        """_summary_
            Método para validar se a jogada é válida.

            xInicial: Eixo X da casa inicial.
            yInicial: Eixo Y da casa inicial.
            xFinal: Eixo X da casa final.
            yFinal: Eixo Y da casa final.
            jogador: Instância do jogador.
        """
    def validarMovimento(self, xInicial, yInicial, xFinal, yFinal, jogador):
        print(self.casas[7 - xInicial][yInicial])
        if (self.casas[7 - xInicial][yInicial] == jogador.nome):
            print('Movimento Válido')
        else:
            print('Movimento Inválido')

    def printarTabuleiro(self):
        for n in range(0, len(self.casas)):
            print(n, self.casas[n], sep=' ')
        print('   1  2  3  4  5  6  7  8')