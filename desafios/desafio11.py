"""
Faça um programa que mostre a altura e largura de uma parede
e mostre o quanto de tinta será necessária considere um litro
por 2m²
"""

altura = float(input('Escreva a altura em metros [M] '))
largura = float(input('Escreva a largura em metros [M] '))

mq = altura * largura
print(f'Para uma parede de {altura}x{largura}M tem uma área de {altura*largura}m² e será necessário ', end='')
print(f'O total de tinta necessária será de {mq/2}L (Litros)')
