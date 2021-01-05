"""
Crie um programa que leia vários números e coloque em uma
lista e depois crie duas listas extras que conteram apenas os valores pares
e outra com os valores ímpares.
"""
from random import shuffle
lista = []
pares = []

while True:
    i = int(input('Escreva um número '))
    if i % 2 == 0:
        pares.append(i)
    else:
        lista.append(i)
    conti = str(input('Quer continuar? [Y/n] ')).lower()
    if 'n' in conti:
        break
list2 = pares+lista
shuffle(list2)
print(f"""
A lista completa é {list2}
Somente com números pares {pares}
Somente os números ímpares {lista}
""")

