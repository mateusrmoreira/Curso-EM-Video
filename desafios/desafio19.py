""" 15/03/2020 jan Mesu
Um professor faz um programa para sortear o nome de um aluno
para apagar o quadro, motre o nome do sorteado
"""
from random import choice

nome1 = input('Digite o nome de um aluno ')
nome2 = input('Digite o nome de um aluno ')
nome3 = input('Digite o nome de um aluno ')
nome4 = input('Digite o nome de um aluno ')

arr = [nome1,nome2,nome3,nome4]

print(f'O aluno escolhido foi {choice(arr)}')