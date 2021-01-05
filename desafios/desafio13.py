"""
Faça um algoritmo que peça o valor
do salário de um funcionário e mostre com 15% de desconto
"""

salario = float(input('Digite o valor do salário do funcionário\nR$ '))
salario += salario * 0.15
print(f'O salário atual será de {salario:.2f}')