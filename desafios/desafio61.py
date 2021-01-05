"""
Refaça o desafio 51 com uma 
estrutura while
"""
primeiro = int(input('Escreva o primeiro termo '))
razao  = int(input('A razão da PA '))
decimo = primeiro + (10-1) * razao
print(f'O primeiro número é {primeiro} E a razão é {razao}\nestes são os 10 primeiros termos')

while primeiro <= decimo:
    primeiro += razao
    print(primeiro, end=' → ')
