from time import sleep


PAREDE = '#'
CAMINHO_LIVRE = ' '
CAMINHO_PERCORRIDO = "2"
ROBO = "4"
SAIDA = "S"

CAMINHO = ["CIMA", "CIMA", "DIREITA"]

ESQUERDA = [0, -1]
DIREITA  = [0, 1]
CIMA     = [-1, 0]
BAIXO    = [1, 0]

LABIRINTO = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], 
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], 
    ['#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#'], 
    ['#', '#', '#', '#', '#', '#', ' ', ' ', '4', ' ', ' ', ' ', '#', '#', '#', '#', ' ', ' ', ' ', '#'], 
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', '#'], 
    ['#', '#', '#', '#', '#', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'], 
    ['#', '#', ' ', ' ', ' ', ' ', '#', '#', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#', '#', ' ', '#'], 
    ['#', ' ', ' ', '#', ' ', '#', '#', '#', ' ', '#', '#', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#'], 
    ['#', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', '#', '#', ' ', ' ', '#'], 
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 'S', '#']
]


def print_labirinto():
    
    """Imprime o labirinto para o jogo."""

    print("")                   #printa uma linha em branco
    for linha in LABIRINTO:     #por causa do for as linhas ficaram uma embaixo da outra
        print("".join(linha))       #juntou os elementos de cada linha do labirinto e printou o labirinto
    print("")


def movimento(posicao: tuple, direcao: list):

    """Devolve a posição atualizada do robô após a movimentação em uma direção.
    
    Args:
        posicao (tuple): posição atual do robô
        direcao (list): direção a ser percorrida pelo robô

    Returns:
        list: posição do robô após a execução do movimento
    """

    LABIRINTO[posicao[0]][posicao[1]] = CAMINHO_PERCORRIDO      #substitui por 2
    LABIRINTO[posicao[0] + direcao[0]][posicao[1] + direcao[1]] = ROBO
    return [posicao[0] + direcao[0], posicao[1] + direcao[1]]
    

def verifica_movimento(posicao: tuple, direcao: list) -> bool:

    """Verifica se o robô chegou até a saída.
    
    Args:
        posicao (tuple): posição atual do robô
        direcao (list): direção a ser percorrida pelo robô

    Returns:
        bool: True se o robô chegou a saída e imprime SUCESSO.
        False caso contrário, indica que o caminho está livre.
    """

    if LABIRINTO[posicao[0] + direcao[0]][posicao[1] + direcao[1]] == SAIDA:
        
        LABIRINTO[posicao[0] + direcao[0]][posicao[1] + direcao[1]] = ROBO
        LABIRINTO[posicao[0]][posicao[1]] = CAMINHO_PERCORRIDO 

        print_labirinto()
        raise print("SUCESSO")

    return (LABIRINTO[posicao[0] + direcao[0]][posicao[1] + direcao[1]] == CAMINHO_LIVRE) 


def main():

    """Movimenta o robô dentro do labirinto e imprime o jogo."""
    
    POSICAO_INICIAL = [3, 8]         #linha 3 coluna 8

    #acessa a linha na posição 3 e o item da linha na posição 8 e coloca o robô
    LABIRINTO[POSICAO_INICIAL[0]][POSICAO_INICIAL[1]] = ROBO
    print_labirinto()

    POSICAO_ATUAL = POSICAO_INICIAL

    LISTA_MOVIMENTOS = [[2, CIMA], [8, DIREITA], [2, BAIXO], [2, DIREITA], [7, BAIXO]]

    for etapa in LISTA_MOVIMENTOS:

        for _ in list( range(etapa[0]) ):

            if verifica_movimento(POSICAO_ATUAL, etapa[1]):
                POSICAO_ATUAL = movimento(POSICAO_ATUAL, etapa[1])
                print_labirinto()
                sleep(1)


if __name__ == "__main__":
    main()

