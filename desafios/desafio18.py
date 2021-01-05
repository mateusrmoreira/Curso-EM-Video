"""
Faça um programa que leia um âgulo
e mostre o valor do seno, cosseno, e tangente desse ângulo
"""

from math import sin, cos, tan, radians

angulo = int(input('Escreva um ângulo\nPara descobrir o seno cosse e tangente $ '))
print(f"""O valor do ângulo é {angulo}°
Seu Seno é de {sin(radians(angulo)):.2f}
Seu cosseno é de {cos(radians(angulo)):.2f}
Sua tangente é de {tan(radians(angulo)):.2f}
""")