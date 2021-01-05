"""
faça um programa que leia 3 números e diga o maior e o menor
"""
n1 = int(input('Escreva um número '))
n2 = int(input('Escreva um número '))
n3 = int(input('Escreva um número '))
maior = f'{n1} é o maior'
menor = f'{n1} é o menor valor'
if n2 >= n1 and n2 >= n3:
    maior = f'{n2} é o maior'    
elif n3 >= n1 and n3 >= n2:
    maior = f'{n3} é o maior'
elif n2 <= n1 and n2 <= n3:
    menor = f'{n2} é o menor'
elif n3 >= n1 and n3 >= n2:
    menor = f'{n3} é o menor'
print(maior, menor)