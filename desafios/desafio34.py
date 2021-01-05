"""
Escreva um programa que pergunte o salário de um funcionário e dê
um aumento aos que ganham mais de 1250 aumento de 10%
e os que ganham menos de 1250 um aumento de 15%
"""

salario = int(input('Quanto o funcionário ganha? '))
result = f'O valor do salário é de {salario+(salario * 0.10)}' 
if salario < 1250:
   salario += salario * 0.15
   result = f'O valor do salário é de {salario}' 
print(result)