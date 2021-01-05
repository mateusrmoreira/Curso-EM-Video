"""
Crie um programa que leia vários números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles
"""

numeros = int(input('Escreva um número '))
i = 1
soma = numeros
while numeros != 999:
    soma += numeros
    i+=1
    numeros = int(input('Escreva um número '))

print(f"""Foram
{i} números digitados
{soma} é a soma do total deles
""")
