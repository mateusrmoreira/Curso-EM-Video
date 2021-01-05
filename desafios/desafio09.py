''' 13/03/2020 by jan Mesu
Faça um programa que peça um número inteiro qualquer
e mostre a sua tabuada.
'''

from cores import cores

numero = int(input('Escreva um número para ver a tabuada dele: '))

print(
f"""
1  x {cores['azul']}{numero:>5}{cores['limpar']}
2  x {cores['azul']}{numero*2:>5}{cores['limpar']}
3  x {cores['azul']}{numero*3:>5}{cores['limpar']}
4  x {cores['azul']}{numero*4:>5}{cores['limpar']}
5  x {cores['azul']}{numero*5:>5}{cores['limpar']}
4  x {cores['azul']}{numero*6:>5}{cores['limpar']}
7  x {cores['azul']}{numero*7:>5}{cores['limpar']}
8  x {cores['azul']}{numero*8:>5}{cores['limpar']}
9  x {cores['azul']}{numero*9:>5}{cores['limpar']}
10 x {cores['azul']}{numero*10:>6}{cores['limpar']}
""")