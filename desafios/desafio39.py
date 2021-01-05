"""
Faça um programa que pegue o ano atual
e peça o ano de nascimento de uma pessoa

diga se ele ainda vai se alistar e quanto tempo falta

se passou do ano de se alistar

ou já no ano de se alistar
"""
from datetime import datetime

atual =  datetime.now().year
pessoa = int(input('Digite o ano que você nasceu '))

status = 'Passou do tempo para se alistar'
if atual - pessoa == 18:
   status = 'Está no ano de se alistar'   
elif atual - pessoa <= 0:
    status = f'Faltam {((atual - pessoa)*-1) + 18} para você se alistar'
elif atual - pessoa < 18:
    status = f'faltam {(atual-pessoa)} anos para se alistar'
print(status)