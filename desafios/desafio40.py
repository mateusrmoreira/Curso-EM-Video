"""25/03/2020 jan Mesu
Crie um programa que leia 2 notas de um aluno
e diga a sua média

- média abaixo de 5.0 REPROVADO
- média entre 5.0 e 6.9 Recuperação
- média superior á 7.0 ele está aprovado
"""

n1 = float(input('Escreva a nota do primeiro semestre # '))
n2 = float(input('Escreva a nota do segundo  semestre # '))
media = (n1+n2) / 2

result = f'Com a média de {media} O Aluno está em recuperação'
if media < 5.0:
   result = f'Com a média de {media} O Aluno está reprovado'
elif media >= 7.0:
   result = f'Com a média de {media} O Aluno está Aprovado'
print(result)