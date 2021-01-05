""" 19/03/2020 jan Mesu
Coloque o ano bissexto 
"""
from datetime import date
ano = int(input('Digite aqui um ano, coloque 0 para o ano atual '))

if ano == 0:
    ano = date.today().year
    print('o ano atual ')
if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
   print('É um ano bissexto ano') 
else:
    print('Não é um ano bissexto')