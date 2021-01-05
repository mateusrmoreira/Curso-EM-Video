"""
Desenvolva um programa que peça
nome, idade e sexo de quatro pessoas
e no final mostre: 
A média de idade 
O nome do homem mais velho
e quantas mulheres tem menos de 21 anos
"""

homem  = ''
mulher = 0
media  = 0
maior  = 0
for i in range(0,4):
    nome  = input('Qual é o seu nome? ') 
    idade = int(input('Digite a sua idade '))
    if i == 0:
       maior = idade 
    sexo  = input('Escreva o seu sexo [M/F] ').lower()
    media += idade
    if sexo in 'Mmasculino' and idade > maior:
       homem = nome  
    elif sexo == 'Ffeminino' and idade < 21:
        mulher += 1
print(f"""
O nome do homem mais velho é {homem}
O total de mulheres com menos de 21 anos são {mulher}
A média de idades são {media/4}
""")