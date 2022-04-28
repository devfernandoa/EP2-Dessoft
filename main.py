import f
from paises import base_dados_paises

tentativas = 20
pais = f.sorteia_pais(base_dados_paises)

jogar_dnv = "sim"

while jogar_dnv == "sim":
    while tentativas > 0:
        print('\033[0;37;40mVocê tem {} tentativas'.format(tentativas))
        s = input('\n\033[0;37;40mQual seu chute? ')
        #dá uma dica para o jogador
        if s == "dica":
            #adicionar código das dicas
            continue
        #dá a resposta se o jogador desiste
        elif s == "desisto":
            print("Você desistiu! O país era " + pais)
            break
        #recebe um chute normal
        elif s == pais:
            print('\n\033[0;32;40mParabéns, você acertou!')
            break
        #recebe um chute inválido
        elif s not in base_dados_paises.keys():
            print('chute inválido')
        else:
            print('\n\033[0;31;40mErrou!')
            tentativas -= 1
    #pergunta se o jogador quer reiniciar o jogo
    jogar_dnv = print((input("Você quer jogar de novo?")).lower)