"""
Faça um programa que peça o nome e média de um aluno
no final mostre e situação de cada um deles.
"""
print('-='*15)
print(f'{"Old School":^30}')
print('-='*15)

nome = str(input('Escreva o nome do aluno '))
media = float(input('Escreva a média do aluno '))

aluno = dict()
aluno['Nome'] = nome
aluno['media'] = media
aluno['situacao'] = 'RECUPERAÇÃO'

if media < 6:
    aluno['situacao'] = 'REPROVADO'
elif media >= 7:
    aluno['situacao'] = 'APROVADO'

for k, v in aluno.items():
    print(f'{k}: {v}')

