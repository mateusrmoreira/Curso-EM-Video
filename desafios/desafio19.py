"""
Faça um programa de um professor na sala de aula
que quer sortear que vai apagar o quadro
"""
from random import choice
aluno1 = input('Nome do aluno(a) ')
aluno2 = input('Nome do aluno(a) ')
aluno3 = input('Nome do aluno(a) ')
aluno4 = input('Nome do aluno(a) ')

lista = aluno1,aluno2,aluno3,aluno4

print(f'O aluno escolhido foi {choice(lista)}')