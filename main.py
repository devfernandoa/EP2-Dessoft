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

    #variaveis mercado de dicas
    lista_dicas = {}
    letras_restritas = []
    cor_compra = False
    area_compra = False
    cont_compra = False
    pop_compra = False
    preco = int()
    capital = base_dados_paises[pais]['capital']
    area = base_dados_paises[pais]['area']
    cont = base_dados_paises[pais]['continente']
    pop = base_dados_paises[pais]['populacao']
    cor_band = f.cor_bandeira(base_dados_paises[pais]['bandeira'])

    #loop principal
    while tentativas > 0:
        print('\n' + cor.preto  + cor.negrito + 'Você tem {} tentativas'.format(tentativas) + cor.fim)

        #recebe o input do jogador
        chute = input('\n' + cor.preto  + cor.negrito + 'Qual seu chute? ' + cor.fim)

        #dá uma dica para o jogador
        if (chute == "Dica".lower()):
            print('Você está no mercado de dicas, onde você pode comprar dicas por tentativas\n 1. Cor da bandeira  - Custa 4 tentativas\n 2. Letra da capital  - Custa 3 tentativas\n 3. Area do pais  - Custa 6 tentativas\n 4. Nome do continente  - Custa 7 tentativa\n 5. População  - Custa 5 tentativas\n Se quiser sair do mercado de dicas, digite 0.\n')
            dica = input('Digite o número da dica que você quer comprar: ')
            if dica == '0':
                print('Você saiu do mercado de dicas.')

            #Lógica de comprar a cor da bandeira
            elif dica == '1':
                preco = 4
                if cor_compra or preco >= tentativas:
                    print('\n' + cor.vermelho + 'Isso não é possível!' + cor.fim + '\n')
                    continue
                else:
                    lista_dicas['cor'] = (('A cor da bandeira é ' + str(cor_band)))
                    tentativas -= preco
                    cor_compra = True

            #Lógica de comprar a letra da capital
            elif dica == '2':
                preco = 3
                if len(f.remove_duplicadas(list(capital), len(capital))) == len(letras_restritas) or preco >= tentativas:
                    print('\n' + cor.vermelho + 'Isso não é possível!' + cor.fim + '\n')
                    continue
                else:
                    letras_restritas.append(f.sorteia_letra(capital, letras_restritas))
                    tentativas -= preco
                lista_dicas['letra'] = (('Letras da capital: ' + ', '.join(letras_restritas)))
            
            #Lógica de comprar a area do pais
            elif dica == '3':
                preco = 6
                if area_compra or preco >= tentativas:
                    print('\n' + cor.vermelho + 'Isso não é possível!' + cor.fim + '\n')
                    continue
                else:
                    lista_dicas['area'] = (('A area do país é ' + str(area)))
                    tentativas -= preco
                    area_compra = True

            #Lógica de comprar o nome do continente
            elif dica == '4':
                preco = 7
                if cont_compra or preco >= tentativas:
                    print('\n' + cor.vermelho + 'Isso não é possível!' + cor.fim + '\n')
                    continue
                else:
                    lista_dicas['continente'] = (('O continente do pais é ' + str(cont)))
                    tentativas -= preco
                    cont_compra = True

            #Lógica de comprar a população
            elif dica == '5':
                preco = 5
                if pop_compra or preco >= tentativas:
                    print('\n' + cor.vermelho + 'Isso não é possível!' + cor.fim + '\n')
                    continue
                else:
                    lista_dicas['populacao'] = (('A população do pais é ' + str(pop)))
                    tentativas -= preco
                    pop_compra = True
            else:
                print('\n' + cor.vermelho + 'Isso não é possível!' + cor.fim + '\n')
                continue
            #loop para imprimir as dicas
            for i in lista_dicas.values():
                print(i)
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
        if chute != pais:
            print('\n' + cor.vermelho + 'Você errou!\n' + cor.fim)

            #adiciona a tentativa à lista de tentativas
            lista_paises = f.adiciona_em_ordem(chute, d, lista_paises)
            lista_chutes.append(chute)

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
            continue

    #finaliza o jogo quando acabam as tentativas
    if tentativas == 0:
        print("Acabaram suas tentativas. Você perdeu! O país sorteado era " + pais)

    #pergunta se o jogador quer reiniciar o jogo

    jogar_dnv = input(cor.negrito + '\n' + "Você quer jogar de novo? (sim ou nao) " + cor.fim + '\n')
#finalização quando o jogar não deseja jogar novamente
print('Obrigado por jogar!')