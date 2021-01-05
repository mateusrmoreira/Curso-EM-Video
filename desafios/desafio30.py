""" 18/03/2020 jan Mesu
Faça um programa que verifique se um número é ímpar ou se ele é par
"""
numero = int(input('Escreva um número qualquer '))

if numero == 0:
        print('O número 0 é neutro')
elif numero % 2 == 0:
    print(f'Você digitou {numero} e ele é par')
else:
    print(f'O número {numero} é ímpar')    