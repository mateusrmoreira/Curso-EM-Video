""" 18/03/2020 jan Mesu
Faça um jogo de advinhar 
"""
from random import randint

user = int(input('Advinha o número que estou pensando de 0 à 10! '))
computer = randint(0,10)

if user == computer:
    print(f'Eu pensei {computer} e você acertou!!')
else: 
    print(f'Eu pensei {computer} e você pensou {user}!!')    