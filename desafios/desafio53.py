"""
Crie um programa que leia uma frase qualquer
e diga se ela é um palíndromo
"""
palavra = input('Escreva uma frase ').strip().lower()

if palavra.replace(' ', '') == palavra.replace(' ', '')[::-1]:
   print(f'A frase {palavra} é palíndroma') 