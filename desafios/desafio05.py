''' 13/03/2020 by jan Mesu
Faça um programa que peça um número inteiro e mostre na tela
seu sucessor e seu antecessor
'''

from cores import cores 
numero = int(input(f'{cores["verde"]}Escreva um número inteiro {cores["limpar"]} '))

print(f'O número digitado foi {numero} \nO Seu antecessor é {numero-1}\nE Seu sucessor é {numero+1}')