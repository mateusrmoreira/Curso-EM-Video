"""
Desenvolva um programa que leia 
um número inteiro e mostre o primeiro
termo e a razão de uma PA. no final
mostre os 10 primeiros termos
"""

primeiro = int(input('Escreva o primeiro termo '))
razao  = int(input('A razão da PA '))
decimo = primeiro + (10-1) * razao
print(f'O primeiro número é {primeiro} E a razão é {razao}\nestes são os 10 primeiros termos')
for i in range(primeiro, decimo+razao, razao):
    print(i, end=' → ')
print('\n')