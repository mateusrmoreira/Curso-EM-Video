"""
"""


numeros = soma = i = 0

while True:
    numeros = int(input('Escreva um número '))
    if numeros == 999:
        break

    soma += numeros
    i+=1

print(f"""Foram digitados
{i} números e a soma do total deles é {soma}
""")