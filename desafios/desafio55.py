"""
Faça um programa que leia o peso
de cinco pessoas e diga quem foi o maior peso
e o menor peso
"""
maior = 0
menor = 0
for i in range(0,7):
    peso = int(input('Digite o seu peso '))
    if i == 1:
       maior = peso
       menor = peso
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso 
print(f'O maior peso é {maior}\nO menor peso é {menor}')