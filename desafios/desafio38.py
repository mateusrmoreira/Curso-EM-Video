"""
Escreva um programa que leia dois 
números e compare mostrando as seguintes mensagem

o primeiro valor é o maior

o segundo valor é o maior

ou se são iguais
"""

numero1  = int(input('Escreva um número '))
numero2  = int(input('Escreva um número (eu sei de novo) '))
maior = f'Primeiro {numero1} número é o maior'
if numero2 > numero1:
    maior = f'Segundo {numero2} número é o maior'
elif numero1 == numero2:
    maior = f'{numero1} e {numero2} são iguais'    
print(maior)