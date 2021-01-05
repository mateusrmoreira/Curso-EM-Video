"""
Um professor que sortear a ordem de apresentação
de um trabalho
"""
from random import shuffle

aluno1 = input('Nome do aluno(a) ')
aluno2 = input('Nome do aluno(a) ')
aluno3 = input('Nome do aluno(a) ')
aluno4 = input('Nome do aluno(a) ')

lista = [aluno1,aluno2,aluno3,aluno4]

shuffle(lista)
print(f'A ordem de apresentação foi {lista}')