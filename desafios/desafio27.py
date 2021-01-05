""" 16/03/2020 jan Mesu
Faça um programa que leia o nome completo de uma pessoa
e diga o primeiro nome e o último nome separadamente
"""

nome = str(input('Escreva o seu nome completo :> ')).split()

print(f'Seu primeiro nome é {nome[0].title()}\nE seu último nome é {nome[-1].title()}')