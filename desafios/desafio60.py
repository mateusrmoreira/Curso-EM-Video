"""
Faça um programa que leia um número
qualquer e mostre o seu fatorial
"""

numero = float(input('Escreva um número para ver seu fatorial '))
i = numero
f = 1
while i > 0:
    print(f'{i}', end='')
    print(' x ' if i > 1 else ' = ', end='')
    f *= i
    i-=1
print(f'{f}\nfim')
