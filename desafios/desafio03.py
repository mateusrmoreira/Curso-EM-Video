''' 13/03/2020 by jan Mesu
Faça um programa que peça dois números e mostre a soma deles
'''
from cores import cores

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
s  = f'{cores["amarelo"]}{n1 + n2}{cores["limpar"]}'

print(f'A soma entre {n1} e {n2} gerou o resultado de {s}')