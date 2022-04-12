from time import sleep


PAREDE = '#'
CAMINHO_LIVRE = ' '
CAMINHO_PERCORRIDO = "2"
ROBO = "4"
SAIDA = "S"

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


def print_labirinto() -> list[list]:
    """Imprime o labirinto para o jogo.
    
    Returns:
        list[list]:  lista de listas com caminhos do jogo.
    """
    print("")
    for linha in LABIRINTO:
        print("".join(linha))   
    print("")


def movimento(posicao: tuple, direcao: list) -> list:
    """Devolve a posição atualizada do robô após a movimentação em uma direção.
    
    Args:
        posicao (tuple): posição atual do robô
        direcao (list): direção a ser percorrida pelo robô

    Returns:
        list: posição do robô após a execução do movimento
    """
    LABIRINTO[posicao[0]][posicao[1]] = CAMINHO_PERCORRIDO
    LABIRINTO[posicao[0] + direcao[0]][posicao[1] + direcao[1]] = ROBO
    return [posicao[0] + direcao[0], posicao[1] + direcao[1]]
    

def verifica_movimento(posicao: tuple, direcao: list) -> bool:
    """Verifica se o robô chegou até a saída.
    
    Args:
        posicao (tuple): posição atual do robô
        direcao (list): direção a ser percorrida pelo robô

    Returns:
        bool: True se o robô chegou a saída, imprimindo SUCESSO.
        False caso contrário, indicando que o caminho ainda está livre.
    """

    if LABIRINTO[posicao[0] + direcao[0]][posicao[1] + direcao[1]] == SAIDA:
        LABIRINTO[posicao[0]][posicao[1]] = CAMINHO_PERCORRIDO
        LABIRINTO[posicao[0] + direcao[0]][posicao[1] + direcao[1]] = ROBO
        print_labirinto()
        print("SUCESSO")
        
    return (LABIRINTO[posicao[0] + direcao[0]][posicao[1] + direcao[1]] == CAMINHO_LIVRE) 


def main() -> None:
    """Movimenta o robô dentro do labirinto e imprime o jogo."""

    POSICAO_INICIAL = [3, 8]

    LABIRINTO[POSICAO_INICIAL[0]][POSICAO_INICIAL[1]] = ROBO

    print_labirinto()

    POSICAO_ATUAL = POSICAO_INICIAL

    for i in list(range(2)):
        if verifica_movimento(POSICAO_ATUAL, CIMA):
            POSICAO_ATUAL = movimento(POSICAO_ATUAL, CIMA)
            print_labirinto()
            sleep(1)

    for i in list(range(8)):
        if verifica_movimento(POSICAO_ATUAL, DIREITA):
            POSICAO_ATUAL = movimento(POSICAO_ATUAL, DIREITA)
            print_labirinto()
            sleep(1)
    
    for i in list(range(2)):
        if verifica_movimento(POSICAO_ATUAL, BAIXO):
            POSICAO_ATUAL = movimento(POSICAO_ATUAL, BAIXO)
            print_labirinto()
            sleep(1)

    for i in list(range(2)):
        if verifica_movimento(POSICAO_ATUAL, DIREITA):
            POSICAO_ATUAL = movimento(POSICAO_ATUAL, DIREITA)
            print_labirinto()
            sleep(1)      

    for i in list(range(7)):
        if verifica_movimento(POSICAO_ATUAL, BAIXO):
            POSICAO_ATUAL = movimento(POSICAO_ATUAL, BAIXO)
            print_labirinto()
            sleep(1)

    return None

if __name__ == "__main__":
    main()

