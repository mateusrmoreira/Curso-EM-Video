""" 19/03/2020 jan Mesu
Faça um programa que peça 3 valores e diga
qual é o maior e qual é o menor deles?
"""
a = int(input('Digite um número '))
b = int(input('Digite um número '))
c = int(input('Digite um número '))

maior = a
menor = c

if b < a and b < c:
   menor = b
if a < b and a < c:
   menor = a   
if b > a and b > c:
   maior = b 
if c > a and c > b:
   maior = c 

print(f'O maior foi {maior} e o menor foi {menor}')
    