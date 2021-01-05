"""
Faça um programa que calcula emprestimo 
para a compra de uma casa, calcule o valor da casa
O salário do comprador e quantos anos irão ser pagos

calcule o valor da prestação sabendo que não poderá passar
de 30% do salário, se não o imprestimo será negado.
"""
casa = float(input('Digite o valor da casa R$ '))
anos = float(input('quantos anos pretende pagar? ')) * 12
salario =  float(input('Salário mensal do comprador '))
media = casa / anos

status = 'Aprovado'

if salario * 0.30 < media:
   status = 'Reprovado' 
print(f'O emprestimo para a compra da casa foi {status}')   