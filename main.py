import f
from paises import base_dados_paises
from cores import cor

raio = 6371

jogar_dnv = "sim"

while jogar_dnv == "sim":

    pais = f.sorteia_pais(base_dados_paises)

    tentativas = 20
    lista_chutes = []
    lista_paises = []

    while tentativas > 0:
        print('\n' + cor.preto  + cor.negrito + 'Você tem {} tentativas'.format(tentativas) + cor.fim)
        s = input('\n' + cor.preto  + cor.negrito + 'Qual seu chute? ' + cor.fim)

        #dá uma dica para o jogador
        if s == "dica":
            #adicionar código das dicas
            continue

        #dá a resposta se o jogador desiste
        elif s == "desisto":
            print("Você desistiu! O país era " + pais)
            break
        #recebe um chute normal
        if s == pais:
            print('\n' + cor.verde + cor.negrito + 'Parabéns, você acertou!' + cor.fim)
            break

        #recebe um chute inválido
        elif s not in base_dados_paises.keys():
            print('chute inválido')
        else:
            print('\n' + cor.vermelho + 'Você errou!\n' + cor.fim)

            tentativas -= 1
    #pergunta se o jogador quer reiniciar o jogo
    jogar_dnv = print((input("Você quer jogar de novo?")).lower)