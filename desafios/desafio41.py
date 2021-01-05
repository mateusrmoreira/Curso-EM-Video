""" 25/03/2020 jan Mesu
A confederação nacional de natação
precisa de um programa para selecionar a categoria de um atleta

Até 9 mirim
Até 14 ele é Infantil
Até 19 anos ele é Junior
Até 25 anos ele é Sênior
Até acima de 25 ele é master
"""
from datetime import datetime

nascimento = int(input('Qual é seu ano de nascimento do atleta ? '))
idade = datetime.now().year - nascimento


result = 'Mirim'
if idade > 9 and idade <= 14:
   result = 'Infantil' 
elif idade > 14 and idade <= 18:
   result = 'Junior'
elif idade > 19 and idade <= 24:
   result = 'Sênior'
elif idade >= 25:
   result = 'Master'

print(f'O atleta tem {idade} anos é a sua categoría é {result}')