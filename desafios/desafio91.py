"""
Crie um programa que peça 4 jogadores a jogar números aleatórios
No final coloque os dicionários em ordem mostrando o vencedor c-
om o maior número.
"""

from random import randint
from time import sleep
from operator import itemgetter

jogo = {
    'jogador1': randint(1,7),
    'jogador2': randint(1,7),
    'jogador3': randint(1,7),
    'jogador4': randint(1,7)}
ranking = dict()
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(0.2)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-'*30)
print(f'{"RANKING":^30}')
print('-'*30)
for i, v in enumerate(ranking):
    print(f'{i+1:>8} {v[0]}: {v[1]}')