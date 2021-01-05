"""
Faça um programa que leia o cateto oposto e do adjacente
e calcule a hipotenusa
"""
from math import hypot
co = float(input('Digite o valor do cateto oposto $ '))
ca = float(input('Digite o valor do cateto adjacente $ '))

print(f'O valor da hipotenusa é {hypot(co,ca):.2f}')
