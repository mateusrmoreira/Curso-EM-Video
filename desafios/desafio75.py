"""
Escreva um programa que peça 4 valores no teclado
e guarde-os em uma tupla no final mostre:

A) Quantas vezes foram digitadas o número 9
B) Em que posição está o número 3
C) Quais números são pares
"""
tabela = (
    int(input('Escreva um número ')),
    int(input('Escreva um outro número ')),
    int(input('Escreva mais um número ')),
    int(input('Escreva o último número ')),
)

print(f"""
Os números digitados foram {tabela}
O número 9 apareceu {tabela.count(9)}""")

if 3 in tabela:
    print(f'número trez aparece na posição {tabela.index(3)+1}')
par = 0
for i in tabela:
    if i % 2 == 0:
        par += 1
print(f'foram encontrados {par} números pares ')

