"""
Faça um programa que leia o sexo de
uma pessoa nos formatos F e M se  a
pessoa não informar F ou M o programa 
pede para ela digitar corretamente
"""

sexo = str(input('Informe seu sexo [M/F] ')).lower()

while sexo not in 'fm':
    sexo = str(input('Por favor informe um valor válido [M/F] ')).lower()
print(f'Seu sexo registrado como {sexo}, obrigado') 