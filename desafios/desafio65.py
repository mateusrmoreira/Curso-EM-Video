"""
Crie um programa que leia vários números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""
continuequestion = ''
maior, menor, soma, i = 0, 0, 0, 0

while continuequestion != 'n':
       
    number = int(input('Escreva um número ')) 
    if i == 0:
       menor = number
       maior = number
    elif number > maior:
        maior = number 
    elif number < menor:
        menor = number    
    soma += number
    i+=1
    
    continuequestion = str(input('Você quer continuar? [S/n] ')).lower()

print(f'A média de todos os números é {soma/i}\nO Maior número foi {maior}\nO menor número foi {menor}')
