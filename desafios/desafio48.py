"""
faça um programa que some todos os números 
ímpares que são múltiplos de 3 entre 1 e 500
"""
soma = 0
cont = 0
for i in range(1,501, 2):
    if i % 3 == 0:
      soma += i
      cont += 1

print(f'A soma de todos os {cont} valores solicitados é {soma}')