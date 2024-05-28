
def partida():
    n = int(input('valor total de peças: '))
    m = int(input('Qtde maxima de peças por rodada: '))
    jogador_incia = False
    fim_partida = False
    if n % (m+1) == 0:
        print("Você começa!")
        jogador_incia = True
    else:
        print("Computador começa!")
    
    while True:
        if jogador_incia:
            usuario_escolhe_jogada(n,m)
            computador_escolhe_jogada(n,m)
        else:
            computador_escolhe_jogada(n,m)
            usuario_escolhe_jogada(n,m)
        
        
def computador_escolhe_jogada(n,m):
    ...

def usuario_escolhe_jogada():
    ...