"""
Faça um programa que leia um ano qualquer
e diga se é um ano bissexto
"""
from datetime import date

ano = int(input('Escreva um ano digite 0 para o ano atual\n$ '))
result = f'{ano} não é um ano bissexto' 

if ano == 0:
   ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
   result = f'{ano} é um ano bissexto' 
else:
   result = f'{ano} não é um ano bissexto'   
print(result)