"""
Crie um programa tenha uma túpla com várias pelavras
e no final mostre a palavra com as vogais que tem nela
"""

tabela = ('Canelinha', 'maça', 'tomate', 'yx','yahoo', 'futebol','casca', 'python','gratis')
letras = ''
for i in tabela:
    print(f'\nPara a palavra {i} ', end='')
    for c in i:
        if c in 'aeiou':
           print(c, end='')
print()