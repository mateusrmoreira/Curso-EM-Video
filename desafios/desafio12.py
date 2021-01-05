''' 13/03/2020 by jan Mesu
Faça um programa que leia o preço de um produto e mostre o seu nome preço com
5% de desconto
'''
preço    = float(input('Preço do produto R$ '))

desconto = preço * 5/100

print(f'Preço do produto de R${preço} com o desconto de 5% R${desconto:.2f}, o preço no fim dica R$ {desconto+preço:.2f}')