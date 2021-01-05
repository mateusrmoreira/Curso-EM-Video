""" 25/03/2020 jan Mesu
Analisando triângulos peça os 3 segmetos
E mostre se eles formam um triangulo

E diga se ele é équilátero com todos os lados iguais
Se é Isósceles com dois lados iguais ou 
Escaleno com todos os lados diferentes
"""

seg1 = float(input('Primeiro Segmento '))
seg2 = float(input('Segundo Segmento '))
seg3 = float(input('Terceiro Segmento '))

if seg1 <= (seg2+seg3) and seg2 <= (seg1+seg2) and seg3 <= (seg1+seg2):
    if seg1 == seg2 == seg3:
      result = 'iquilátero' 
    elif seg3 != seg1 != seg2:
      result = 'Isósceles'
    else:
      result = 'Escaleno'
    print(f'os segmentos forma um triangulo {result}')
else:
    print('Não forma triângulo')
