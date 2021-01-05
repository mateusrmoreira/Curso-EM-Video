"""
Faça o desafio 86 mas agora mostre
A) A soma de todos os valores pares digitados
B) A soma dos valores da terceira coluna
C) O maior valor da segunda coluna
"""
matriz = [[0,0,0],[0,0,0],[0,0,0]]
pares = coluna = coluna_dois = 0
for i in range(0,3):
    for c in range(0,3):
        matriz[i][c] = int(input(f'Digite um valor para [{i}, {c}]: '))
        if matriz[i][c] % 2 == 0:
            pares += matriz[i][c]
 
        if i == 1 and matriz[i][c] > coluna_dois:
           coluna_dois = matriz[i][c]
    
        if c == 2:
            coluna += matriz[i][c]

# print
for i in range(0,3):
    for c in range(0,3):
      print(f'[{matriz[i][c]:^5}]', end='')
    print()
print(f"""
A soma de todos os valores pares é {pares}
A soma de todos os valores da 3° coluna é {coluna}
O maior valor da 2° coluna {coluna_dois}
""")