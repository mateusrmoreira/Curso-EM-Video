''' 13/03/2020 by jan Mesu
Faça um programa que peça a altura da parede em metros e diga o quanto de tinta é necessário.
Sabendo que cada litro de tinta pinta 2m²  
'''
largura  = float(input('Largura da  parede  em metros '))

altura   = float(input('Altura  da  parede  em metros '))

area     = altura * largura

print(f'Sua parede tem uma dimensão de {largura} x {altura}, A sua área é de {area}\nSerá necessário {area/2}L de tinta')