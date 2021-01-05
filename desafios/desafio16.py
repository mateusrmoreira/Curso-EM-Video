"""
Escreva um número real (9.8, 7.987, 100.76)
e mostre sua porção inteira na tela
"""

from math import trunc

num = float(input('Escreva um número real (Número quebrado) $ '))
print(f'A porção inteira de {num} é {trunc(num)}')