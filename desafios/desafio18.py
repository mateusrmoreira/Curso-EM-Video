""" 15/03/2020 jan Mesu
Faça um programa que leia um ângulo e diga
seu seno cosseno e tangente
"""

from math import (
    sin, 
    cos, 
    tan, 
    radians)

angulo = radians(float(input('Qual é o ângulo ')))
print(f'O Seno do ângulo é {sin(angulo):.2f}\nO Cosseno é {cos(angulo):.2f}\nE a tangente é {tan(angulo):.2f}')