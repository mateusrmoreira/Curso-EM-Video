""" 19/03/2020 jan Mesu
Faça um programa que peça o salário de um funcionário, e aplique
um aumento de 10% para quem ganha até R$ 1250, e de 15% para salários inferiores
"""

salario = float(input('Salário do funcionário '))

aumento = (10/100)

if salario <= 1250:
   aumento = (15/100)

print(f'Quem ganhava R$ {salario:.2f} sofreu um aumento salarial para R$ {salario+(salario*aumento):.2f}')
