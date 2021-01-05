"""
Faça um programa que tenha uma função
chamada voto e que receba o ano de na
scimento de uma pessoa no final irá re
tornar O valor litera se ela tem o vot
o NEGADO, OBRIGATORIO, OPCIONAL
"""

def voto(ano):
    from datetime import datetime
    idade = datetime.now().year - ano
    situacao = 'OBRIGADOTÓRIO'
    if idade >= 65:
        situacao = 'OPCIONAL'
    elif idade < 16:
        situacao = 'NEGADO'
    return idade, situacao

ano = int(input('O ano que você nasceu '))

idade, situacao = voto(ano)

print(f'Com a idade de {idade} anos o voto é {situacao}')