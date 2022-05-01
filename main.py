import f
from paises import base_dados_paises
from cores import cor

raio = 6371
jogar_dnv = "sim"

while jogar_dnv == "Sim".lower():

    #print da introdução
    print('Bem vindo ao Insper Paises, o projeto 2 de Design de Software feito por Fernando Alzueta e Ilana Chaia Finger\nAqui seu objetivo é acertar um país sorteado pelo computador, você terá 20 chances para acertar\nA cada tentativa você pode comprar dicas, chutar um país ou desistir\nSe você chutar um país, ele será adicionado em uma lista que possui a distancia entre a capital do pais sorteado e do chute\n')
    print('Comandos: \ndica - entra no mercado de dicas se você ainda tiver dicas disponíveis\ndesisto - sai do programa\ncomandos - exibe os comandos\nchutes - exibe a lista de paises chutados')

    pais = f.sorteia_pais(base_dados_paises)

    #declarando o pais sorteado e sua latitude e longitude
    pais = f.sorteia_pais(base_dados_paises)
    p1 = base_dados_paises[pais]['geo']['latitude']
    l1 = base_dados_paises[pais]['geo']['longitude']

    #outras variáveis básicas
    tentativas = 20
    lista_chutes = []
    lista_paises = []

    #contador de dicas
    dicas = 5

    #loop principal
    while tentativas > 0:
        print('\n' + cor.preto  + cor.negrito + 'Você tem {} tentativas'.format(tentativas) + cor.fim)

        #recebe o input do jogador
        chute = input('\n' + cor.preto  + cor.negrito + 'Qual seu chute? ' + cor.fim)

        #dá uma dica para o jogador
        if (chute == "Dica".lower()) and (dicas > 0):
            dicas -= 1
            #adicionar código das dicas
            continue

        elif (chute == "Dica".lower()) and (dicas <= 0):
            print("Você não tem mais dicas disponíveis.")
            continue

        #dá a resposta se o jogador desiste
        elif chute == "Desisto".lower():
            print("Você desistiu! O país era " + pais)
            break

        #mostra os comandos
        elif chute == "Comandos".lower():
            print('Comandos: \ndica - entra no mercado de dicas se você ainda tiver dicas disponíveis\ndesisto - sai do programa\ncomandos - exibe os comandos\nchutes - exibe a lista de paises chutados')
            continue

        #mostra a lista de países chutados até o momento
        elif chute == "Chutes".lower():
            print(lista_chutes)
            continue

        #recebe um chute válido correto
        elif chute == pais:
            print('\n' + cor.verde + cor.negrito + 'Parabéns, você acertou em apenas ' + str(21-tentativas) + ' tentativas!' + cor.fim)
            break

        #recebe um chute inválido
        elif chute not in base_dados_paises.keys():
            print('chute inválido')
            continue

        #recebe um país que já foi chutado
        elif chute in lista_chutes:
            print('você já chutou esse pais')
            continue

        #declarando latitude e longitude do pais do chute para calcular distância desse país até o país sorteado
        p2 = base_dados_paises[chute]['geo']['latitude']
        l2 = base_dados_paises[chute]['geo']['longitude']

        #calculando distância entre os dois paises
        d = round(f.haversine(raio, p1, l1, p2, l2))

        #recebe um chute válido errado
        elif chute != pais:
            lista_chutes.append(chute)
            print('\n' + cor.vermelho + 'Você errou!\n' + cor.fim)

            #adiciona a tentativa a lista de tentativas
            lista_paises = f.adiciona_em_ordem(chute, d, lista_paises)

            #mostra a lista de paises e distâncias
            print('Distâncias entre os chutes e o país sorteado: ')
            for i in lista_paises:
                if i[1] > 10000:
                    print(cor.roxo + 'pais -> ', i[0], '\ndistancia -> ', str(i[1]) + cor.fim)
                elif i[1] > 5000:
                    print(cor.vermelho + 'pais -> ', i[0], '\ndistancia -> ', str(i[1]) + cor.fim)
                elif i[1] > 1000:
                    print(cor.amarelo + 'pais -> ', i[0], '\ndistancia -> ', str(i[1]) + cor.fim)
                elif i[1] > 0:
                    print(cor.verde + 'pais -> ', i[0], '\ndistancia -> ', str(i[1]) + cor.fim)
            tentativas -= 1

    #finaliza o jogo quando acabam as tentativas
    print("Acabaram suas tentativas. Você perdeu! O país sorteado era " + pais)

    #pergunta se o jogador quer reiniciar o jogo
    jogar_dnv = input("Você quer jogar de novo?")

#finalização quando o jogar não deseja jogar novamente
print('Obrigado por jogar!')