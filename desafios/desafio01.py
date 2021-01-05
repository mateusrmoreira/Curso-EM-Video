''' 12/03/2020 by jan Mesu
Crie um script que, leia o nome de uma pessoa
e mostre uma mensagem de boas vindas com o valor digitado
'''
from cores import cores
nome = input('Olá qual é o seu nome? ')

print(f'Olá {cores["azul"]}{nome}{cores["limpar"]} prazer em te conhecer')
