"""
Crie um programa que leia um número
qualquer e diga se ele é ímpar ou par
"""

numero = int(input('Digite um número '))

result = f'O número {numero} é ímpar'
if numero % 2 == 0:
   result = f'O número {numero} é par'
elif numero == 0:
    result = 'Zero é numero neutro'
print(result)