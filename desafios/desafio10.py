''' 13/03/2020 by jan Mesu
Crie um programa que leia quanto dinheiro a pessoa tem na carteira
e diga quanto ela tem em dólar. Calcular 1 dólar 3,11 reais
'''
from cores import cores

carteira = float(input(f'{cores["azul"]}Quanto dinheiro existe na carteira? R${cores["limpar"]} '))

dolar    = carteira / 3.27

print(f'O total de dinheiro na carteira é R${carteira} Ela tinha ${dolar:.2f} em 2017 na cotação de 3,27')