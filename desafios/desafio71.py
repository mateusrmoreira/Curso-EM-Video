"""
Crie um programa que simule um caixa eletrônico. No início pergunte
O valor que o cliente quer sacar, o programa vai informar quantas
cédulas serão entregues.
"""

valor  = int(input('Quanto você quer sacar? '))

ced1 = ced10 = ced20 = ced50 = 0
valor_mutante = valor
while True:
    if valor_mutante >= 50:
        valor_mutante -= 50
        ced50+=1
    elif valor_mutante >= 20:
        ced20+=1
        valor_mutante -= 20
    elif valor_mutante >= 10:
        ced10+=1
        valor_mutante -= 10
    elif valor_mutante >= 1:
        ced1+=1
        valor_mutante -= 1      
    if valor_mutante == 0:
       break
print(f""" O valor de R${valor} será pago com
{ced50} notas de R$50
{ced20} notas de R$20
{ced10} notas de R$10
{ced1} notas de R$1
""")