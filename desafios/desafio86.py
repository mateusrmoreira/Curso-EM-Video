"""
Crie um programa que crie uma matriz de dimensao 3x3
e no final mostre a matriz com os valores preenchid-
os pelo teclado.
"""

matriz = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,3):
    for c in range(0,3):
        matriz[i][c] = int(input(f'Digite um valor para [{i}, {c}]: '))
for i in range(0,3):
    for c in range(0,3):
      print(f'[{matriz[i][c]:^5}]', end='')
    print()  