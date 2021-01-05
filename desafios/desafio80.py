"""
Crie um programa que leia 5 valores
e os mostre em ordem sem usar o sort
"""

lista = []
menor = maior = 0
for i in range(0,5):
    num = int(input('Escreva um número '))
    if i == 0 or num > max(lista):
        lista.append(num)
        print(f'Foi adicionado no final da lista')
        lista.insert(-1, num)  
    else:
        pos = 0
        while pos < len(lista):
          if num <= lista[pos]:
             lista.insert(pos, num)
             break
          pos += 1
print(f'os valores digitados em ordem foram {lista}')
