"""
Faça um algoritmo que peça o preço de um produto e
mostre o seu valor com 5% de desconto
"""

produto = float(input('Escreva o valor do produto R$ '))
print(f'O desconto de 5% foi aplicado R${produto*0.05:.2f} o total fica fica de R${produto - produto*0.05}')