tabuleiro = [0,1,2,3,4,5,6,7,8]

def desenhar_tabuleiro():
    print(tabuleiro[0],'|',tabuleiro[1],'|',tabuleiro[2])
    print('-----------')
    print(tabuleiro[3],'|',tabuleiro[4],'|',tabuleiro[5]),
    print('-----------')
    print(tabuleiro[6],'|',tabuleiro[7],'|',tabuleiro[8])


def jogar(jogada, jogador):
    tabuleiro[jogada] = jogador


def verificar_jogada(jogada):
    if tabuleiro[jogada] == 'x' or tabuleiro[jogada] =='o':
        print('jogada invalida')
        return False
    else:
        return True
    

def verificar_vitoria(jogador):
    combinacoes = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for combinacao in combinacoes:
        print('resultado: ',tabuleiro[combinacao[0]], tabuleiro[combinacao[1]], tabuleiro[combinacao[2]])
        if tabuleiro[combinacao[0]] == tabuleiro[combinacao[1]] == tabuleiro[combinacao[2]] == 'o':
           return True
        
        if tabuleiro[combinacao[0]] == tabuleiro[combinacao[1]] == tabuleiro[combinacao[2]] == 'x':
           return True

        return False 