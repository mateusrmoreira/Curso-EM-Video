"""
Melhore o desafio 61
Mas pedindo para mostrar mais termos 
"""

primeiro = int(input('Escreva o primeiro termo '))
razao  = int(input('A razão da PA '))
decimo = primeiro + (10-1) * razao
print(f'O primeiro número é {primeiro} E a razão é {razao}\nestes são os 10 primeiros termos')
i = 0
while primeiro:
    primeiro += razao
    print(primeiro, end=' → ')
    i+=1

