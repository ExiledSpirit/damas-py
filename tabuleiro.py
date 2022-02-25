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
        if (not self.__limitesTabuleiro__())):
            return false
        if (not self.__validarPosicaoInicial__()):
            return false

    def __validarPosicaoInicial__(self, xInicial, yInicial):
        if (self.casas[7 - xInicial][yInicial] == jogador.nome):
            return true
        return false

    # Valida se algum dos eixos está fora do tabuleiro.
    def __limitesTabuleiro__(self, xInicial, yInicial, xFinal, yFinal):
        if (xInicial > 8 or xFinal > 8 or yInicial > 8 or yFinal > 8):
            return false
        return true

    def printarTabuleiro(self):
        for n in range(0, len(self.casas)):
            print(n + 1, self.casas[n], sep=' ')
        print('   1  2  3  4  5  6  7  8')

    def verificarVencedor(self):
        for i in range(0, len(self.casas)):
            if (1 in self.casas[i]):
                return 1
            elif (2 in self.casas[i]):
                return 2
            else:
                return 0
                