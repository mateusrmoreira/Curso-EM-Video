""" 15/03/2020 by jan Mesu
Crie um programa que converta uma temperatura digitada em graus C° e converta para F°
"""

celcius = float(input('Digite a temperatura em graus Celcius C° '))
formula = celcius * 9/5 + 32

print(f'A temperatura de {celcius} C°\nFica em {formula} F° ')