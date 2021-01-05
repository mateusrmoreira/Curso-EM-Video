"""
Crie um programa que leia
o ano de nascimento de sete pessoas
e diga quantas pessoas ainda não atingiram a
a maior idade e quantas já são maiores
"""
from datetime import date
atual = date.today().year
maior = 0
menor = 0
for i in range(0,7):
    idade = int(input('Digite a sua idade '))
    if atual - idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'O total de pessoas maiores é {maior}\nO total de pessoas menores é {menor}')    