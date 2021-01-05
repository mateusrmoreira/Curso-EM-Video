"""
Crie um programa que 
peça vários valores e no final mostre

A) Quantos números foram digitados
B) A lista de valores em forma decrescente
C) Se o valor 5 está ou não na lista
"""
num = []
continuar = cinco = ''

while True:
    num.append(int(input('Escreva um número ')))

    continuar = str(input('Quer continuar? [S/n] '))
    if 'n' in continuar:
        break

if 5 in num:
    cinco = f'O número cinco aparece na {num.index(5)}° posição'
num.sort(reverse=True)
print(f"""
O total de valores digitados foram {len(num)}
A posição inversa é {num}
{cinco}
""")
    