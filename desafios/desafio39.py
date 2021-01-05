"""25/03/2020 jan Mesu
faça um programa que peça o ano de nascimento de uma pessoa
Consulte a idade e diga se ele vai precisar se alistar
ou se é o ano de se alistar ou se passou a data para se alistar
"""
from datetime import datetime

nascimento = int(input('Qual é seu ano de nascimento? '))
idade = datetime.now().year - nascimento

result = f'Você está completa {idade} anos de idade esse ano, está na hora de se alistar'
if idade < 18:
   result = f'Você está com {idade} anos de idade, ainda faltam {18-idade} anos para você se alistar'
elif idade > 18:
   result = f'Você está com {idade} anos de idade, ainda se passaram {idade-18} anos do seu alistamento'    
print(result)