import f
from paises import base_dados_paises
from cores import cor

raio = 6371
jogar_dnv = "sim"

while jogar_dnv == "sim":

    #print da introdução
    print('Bem vindo ao Insper Paises, o projeto 2 de Design de Software feito por Fernando Alzueta e Ilana Chaia Finger\nAqui seu objetivo é acertar um país sorteado pelo computador, você terá 20 chances para acertar\nA cada tentativa você pode comprar dicas, chutar um país ou desistir\nSe você chutar um país, ele será adicionado em uma lista que possui a distancia entre a capital do pais sorteado e do chute\n')
    print('Comandos: \ndica - entra no mercado de dicas se você ainda tiver dicas disponíveis\ndesisto - sai do programa\ncomandos - exibe os comandos\nchutes - exibe a lista de paises chutados')

    pais = f.sorteia_pais(base_dados_paises)

    #declarando o pais sorteado e sua latitude e longitude
    pais = f.sorteia_pais(base_dados_paises)
    p1 = base_dados_paises[pais]['geo']['latitude']
    l1 = base_dados_paises[pais]['geo']['longitude']

    tentativas = 20
    lista_chutes = []
    lista_paises = []

    while tentativas > 0:
        print('\n' + cor.preto  + cor.negrito + 'Você tem {} tentativas'.format(tentativas) + cor.fim)
        chute = input('\n' + cor.preto  + cor.negrito + 'Qual seu chute? ' + cor.fim)

        #dá uma dica para o jogador
        if chute == "dica":
            #adicionar código das dicas
            continue

        #dá a resposta se o jogador desiste
        elif chute == "desisto":
            print("Você desistiu! O país era " + pais)
            break

        #mostra os comandos
        elif chute == "comandos":
            print('Comandos: \ndica - entra no mercado de dicas se você ainda tiver dicas disponíveis\ndesisto - sai do programa\ncomandos - exibe os comandos\nchutes - exibe a lista de paises chutados')
            continue

        #mostra a lista de países chutados até o momento
        elif chute == "chutes":
            print(lista_chutes)

        #recebe um chute válido correto
        elif chute == pais:
            print('\n' + cor.verde + cor.negrito + 'Parabéns, você acertou!' + cor.fim)
            break

        #recebe um chute inválido
        elif chute not in base_dados_paises.keys():
            print('chute inválido')
            continue
        elif chute in lista_chutes:
            print('você já chutou esse pais')
            continue
        lista_chutes.append(chute)

        #declarando latitude e longitude do pais do chute
        p2 = base_dados_paises[chute]['geo']['latitude']
        l2 = base_dados_paises[chute]['geo']['longitude']

        #calculando distancia entre os dois paises
        d = round(f.haversine(raio, p1, l1, p2, l2))
        #recebe um chute válido errado
        if chute != pais:
            print('\n' + cor.vermelho + 'Você errou!\n' + cor.fim)

            #adiciona a tentativa a lista de tentativas
            lista_paises = f.adiciona_em_ordem(chute, d, lista_paises)

            #mostra a lista de paises e distâncias
            print('distancias: ')
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
    #pergunta se o jogador quer reiniciar o jogo
    jogar_dnv = input("Você quer jogar de novo?").lower()