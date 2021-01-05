"""
Faça um programa que leia uma lista chamada números
e duas funções chamadas sorteia e soma par a primei
ra sorteia 5 números aleatórios e a segunda soma to
dos os números pares sortiados pela primeira função
"""
from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando os 5 valores da lista', end=' ')
    for i in range(0,5):
        n = randint(0,10)
        print(f'{n}', end=' ', flush=True)
        sleep(0.1)
        lista.append(n) 
    return numeros

def somapar(num):
    somapar = 0
    for v in num:
        if v % 2 == 0:
           somapar += v
    return somapar

numeros = list()
sorteia(numeros)

print(f'A soma de todos os valores pares foram {somapar(numeros)}')