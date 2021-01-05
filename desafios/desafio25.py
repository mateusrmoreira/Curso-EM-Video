""" 16/03/2020 jan Mesu
Crie um programa que leia o nome de uma pessoa e diga 
se ela tem SILVA no nome 
"""
nome = str(input('Escreva o teu nome completo :> ')).upper()

print(f'O nome de {nome.title()}\nTem silva no nome? {"SILVA" in nome}')