"""
Crie um programa que leia o nome e o peso de várias
pessoas no final mostre o nome e o peso das pessoas
mais pesadas e das pessoas mais leves e o total de 
Pessoas cadastradas
"""

leves = pesados = i = 0

pessoas = list()
a = list()
leveslist = list()
pesadoslist = list()

while True:
    a.append(input('Nome: '))
    a.append(float(input('Peso: ')))
    pessoas.append(a[:])

    if a[1] > pesados:
        pesados = a[1]
        pesadoslist.clear()
        pesadoslist.append(a[:])
    elif a[1] == pesados:
        pesadoslist.append(a[:])

    if a[1] < leves or leves == 0:
       leves = a[1]
       leveslist.clear()
       leveslist.append(a[:])
    elif a[1] == leves:
        leveslist.append(a[:])
    a.clear()

    i += 1

    continuar = input('Quer continuar? [Y/n] ').lower()    
    if 'n' in continuar:
        break
print(f'O total de pessoas adicionadas foram {i}')
print(f'O menor peso foi de {leveslist[0][1]} e as pessoas cadastradas com este peso foram ', end='')
for i, v in enumerate(leveslist):
    print(leveslist[i][0], end=' ')

print(f'\nO maior peso foi de {pesadoslist[0][1]} as pessoas com este peso foram ', end=' ')
for i, v in enumerate(pesadoslist):
    print(pesadoslist[i][0], end=' ')
print()
