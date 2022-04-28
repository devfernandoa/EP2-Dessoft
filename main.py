import f
from paises import base_dados_paises

tentativas = 20
pais = f.sorteia_pais(base_dados_paises)

while tentativas > 0:
    print('\033[0;37;40mVocê tem {} tentativas'.format(tentativas))
    s = input('\n\033[0;37;40mQual seu chute? ')
    if s == pais:
        print('\n\033[0;32;40mParabéns, você acertou!')
        break
    else:
        print('\n\033[0;31;40mErrou!')
        tentativas -= 1