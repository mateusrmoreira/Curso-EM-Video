"""
Crie um programa que sorteie 5 números
aleatórios e armazene numa túpla e mostre
todos os números e o maior e menor valor
"""
from random import randint
random_tabela = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))

print(f'Os números sorteados foram {random_tabela}')
print(f'\nO maior número foi {max(random_tabela)}\nO menor foi {min(random_tabela)}')   