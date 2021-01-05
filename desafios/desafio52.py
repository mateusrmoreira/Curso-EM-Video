"""
Faça um programa que leia um número inteiro e diga 
se ele é ou não um número primo. 

Números primos são aqueles que somente são divisíveis 
por ele mesmo ou por um
"""
numero = int(input('Escreva um número '))
count = 0
for i in range(1, numero+1):
    if numero % i == 0:
       count += 1  
       print(f'\033[0;32m{i}\033[m', end=' ')
    print(f'\033[0;31m{i}\033[m', end=' ')   
if count > 2:
   print(f'O número {numero} não é primo') 
else:
   print(f'O número {numero} é primo') 