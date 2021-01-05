""" 15/03/2020 jan Mesu
Faça um programa que, peça o catedo oposto e o cateto adjacente de um triângulo
e mostre a hipotenusa.
"""
from math import hypot

cateto_oposto    = float(input('Cateto Oposto '))

cateto_adjacente = float(input('Cateto Adjacente '))

print(f'Com o cateto oposto sendo de {cateto_oposto} e o adjacente sendo de {cateto_adjacente}\nA hipotenusa é {hypot(cateto_oposto,cateto_adjacente):.2f}')

"""
Este programa poderia ser resolvido da seguinte maneira

hypot = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)

A veriavel hypot é faz o calculo da hipotenusa 
"""