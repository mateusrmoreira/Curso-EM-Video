"""
Faça um programa que Crie palpites aleatórios da mega sena.
O programa vai perguntar quantos jogos serão gerados
vai sortear 6 números entre 1 e 60 para cada jogo cadastrando tudo
em uma lista composta.
"""

from random import randint
from time import sleep

print(f'{"Mega da quebrada":^30}')

usuariojogos = int(input('Quantos jogos você quer criar? '))
jogos = list()
for i in range(0,usuariojogos):
    jogoLista = list()
    c = 0
    while True:
        numero = randint(0,60)
        if numero not in jogoLista:
           jogoLista.append(numero)
           c += 1
        if c >= 6:
            break   
    jogos.append(jogoLista[:])
    jogoLista.clear()  


for i, v in enumerate(jogos): 
    v.sort()
    sleep(0.1)
    print(f'Jogo {i+1}: {v} -- Jogos de {len(v)} dígitos')

