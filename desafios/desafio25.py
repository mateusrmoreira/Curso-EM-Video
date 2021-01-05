"""
Crie um programa que leia o nome de uma pessoa
e diga se tem silva no nome
"""
nome = str(input('Escreva seu nome completo ')).strip().lower()
print(f'{nome} tem SILVA no nome? {"silva" in nome}')