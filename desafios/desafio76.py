"""
Escreva um programa com uma única tupla
e mostre o valor de um produto e o preço dele
de forma tabelada
"""
compras = ("Lápiz", 1.90, "Borracha", 0.50, "Mochila", 100)
print('-'*39)
print(f'{"Listagem de compras":^39}')
print('-'*39)
for pos in range(0,len(compras)):
    if pos % 2 == 0:
        print(f'{compras[pos]:.<30}', end='')
    else:
        print(f'R${compras[pos]:>7.2f}')
print('-'*39)