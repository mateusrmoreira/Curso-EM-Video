''' 13/03/2020 by jan Mesu
Desenvolva um programa que peça 2 notas de um aluno
e mostre a sua média
'''
from cores import cores
nota1 = float(input('Nota do aluno 1° semestre '))
nota2 = float(input('Nota do aluno 2° semestre '))



print(f'A média do aluno foi {cores["amarelo"]}{(nota1+nota2)/2:.2f}{cores["limpar"]}')