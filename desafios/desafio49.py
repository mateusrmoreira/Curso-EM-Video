"""
Faça uma tabuada de um número
com o laço for
"""

numero = int(input('Escreva um número para a ver a sua tabuada '))

for i in range(1,11):
    print(f'{numero} x{i:< 3} ={numero*i:< 2}')