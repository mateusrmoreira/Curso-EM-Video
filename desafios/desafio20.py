""" 15/03/2020 jan Mesu
O professor sortiou os alunos e quer que os nomes deles aparecem
na ordem
"""
from random import shuffle

nome1 = input('Digite o nome de um aluno ')
nome2 = input('Digite o nome de um aluno ')
nome3 = input('Digite o nome de um aluno ')
nome4 = input('Digite o nome de um aluno ')
nome5 = input('Digite o nome de um aluno ')
lista = [nome1,nome2, nome3, nome3, nome4, nome5]
shuffle(lista)
print(f"A lista de alunos para apagar o quadro na semana será {lista}")