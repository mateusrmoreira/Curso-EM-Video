''' 13/03/2020 by jan Mesu
Faça um algoritimo que peça o salário de um funcionário
e mostre o novo valor com 15% de aumento.
'''

salario    = float(input('Escreva o salário do funcionário R$ '))
nousalario = salario * (15/100) 

print(f'O salário do funcionário de R$ {salario}. após o aumento de 15% passa a ser R$ {salario+nousalario:.2f}')

