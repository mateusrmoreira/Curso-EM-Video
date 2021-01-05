"""
Faça um programa que leia 6 números inteiros
e mostre a soma somente dos que foram pares.
"""
soma = 0
cont = 0
for i in range(0,6):
    n = int(input('Escreva um número inteiro '))
    if n % 2 == 0:
       soma += n 
       cont += 1
print(f'A soma de todos os {cont} números pares foram {soma}')