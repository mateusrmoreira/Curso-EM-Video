"""
Faça um programa que leia 5 valores
e quarde eles em uma lista.

Mostre o maior e o menor valor e suas
respectivas posições na lista.
"""
valores = []
for i in range(0,5):
    valores.append(int(input(f'Escreva um valor na posição {i} ')))
print(f'você digitou os valores {valores}')
menor = []
maior = []
for c, v in enumerate(valores):
    if v  == max(valores):
        maior.append(c)
    if v == min(valores):
        menor.append(c)
print(max(valores), '.'*10, *maior, sep=' ')
print(min(valores), '.'*10, *menor, sep=' ')