"""25/03/2020 jan Mesu
Escreva um programa que peça dois números
e diga qual deles é o maior
Qual deles é o menor ou se os dois são iguais.
"""

n1 = float(input('Escreva a nota do primeiro semestre # '))
n2 = float(input('Escreva a nota do segundo  semestre # '))

result = f'As notas são iguais 1° semestre {n1} 2° semestre {n2}'

if n1 < n2:
   result = f'A nota do segundo semestre {n2} é maior que a do primeiro semestre{n1}'
elif n2 < n1:
    result = f'A nota do primeiro semestre {n1} é maior que a nota do segundo semestre {n2}'

print(result)