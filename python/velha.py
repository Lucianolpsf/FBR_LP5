from funcoes_velha import desenhar_tabuleiro, jogar, verificar_jogada, verificar_vitoria
import os

vencedor = False
desenhar_tabuleiro()
contador = 1
jogador = 'x'

while vencedor == False:

    jogada = int(input('Onde deseja jogar?'))
    os.system('cls')

    retorno = verificar_jogada(jogada)

    if retorno == True:
        jogar(jogada, jogador)
    
    if retorno == False:
        print('jogada invalida')
        contador = contador+1

    desenhar_tabuleiro()

    vencedor = verificar_vitoria(jogador)
    print(vencedor)
    if vencedor == True:
        print('Parabens voce venceu')

    contador = contador+1
    if contador % 2 == 0:
        jogador = 'o'
    else:
        jogador ='x' 