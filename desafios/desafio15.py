"""
Aluguel de carro

Dias R$60 KM rodados R$0.65
"""

dias, km = int(input('quantos dias o carro ficou alugado? ')), float(input('Quantos quilometros foram rodados? '))

preco = (dias*60) + (km*0.15)

print(f'O valor total do aluguel foi de R${preco:.2f}')