''' 14/03/2020 by jan Mesu
Crie um programa que peça um número
e mostre seu dobro, seu triplo e sua raíz quadrada
'''
from cores import cores 

numero       = int(input('Escreva um número: '))
dobro        = numero * 2
triplo       = numero * 3

print(
f"""{cores['verde']} O número digitado foi {numero} {cores['limpar']}

O dobro de {cores['azul']}{numero}{cores['limpar']} é {cores['amarelo']}{dobro}{cores['limpar']}

O triplo de {cores['azul']}{numero}{cores['limpar']} é {cores['amarelo']}{triplo}{cores['limpar']}

A raíz quadrade de {cores['azul']}{numero}{cores['limpar']} é {cores['amarelo']} {float(numero)**0.5:.2f}{cores['limpar']}
""" )