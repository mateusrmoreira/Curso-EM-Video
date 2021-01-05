"""
Faça um programa que leia o nome de uma pessoa e mostre em seguida
o primeiro e o último nome separadamente
"""

nome = str(input('Escreva seu nome completo ')).title().split()

print(f" o primeiro nome é {nome[0]} e o último nome é {nome[-1]}")
