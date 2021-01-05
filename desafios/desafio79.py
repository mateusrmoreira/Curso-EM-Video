"""
Crie um programa que receba vários valores
ele não adiciona valores que já existem na
lista e no final mostre todos os valores em
ordem crescente.
"""

lista = []
while True:
    num = int(input('Escreva um número '))
    if num not in lista:
       lista.append(num)
    else:
        print('Número já digitado ')
    continuar = input('Quer continuar? [S/n] ').lower()
    if continuar == 'n':
        break
lista.sort()
print('Todos os números digitados foram', *lista, sep=' ')