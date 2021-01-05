"""
Faça um programa que leia um número inteiro qualquer
e mostre na tela sua tabuada
"""

numero = int(input('Digite o número que você deseja ver a tabuada\n$ '))

for i in range(1,numero+1):
    print(f"{numero} x {i:2} = {i*numero}")