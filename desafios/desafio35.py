""" 20/03/2020 jan Mesu
Analisando triângulos peça os 3 segmetos
E mostre se eles formam um triangulo
"""

seg1 = float(input('Primeiro Segmento '))
seg2 = float(input('Segundo Segmento '))
seg3 = float(input('Terceiro Segmento '))

if seg1 <= (seg2+seg3) and seg2 <= (seg1+seg2) and seg3 <= (seg1+seg2):
    print('os segmentos forma um triangulo')
else:
    print('Não forma triângulo')   