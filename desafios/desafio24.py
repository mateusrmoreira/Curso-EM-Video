"""
Faça um programa que peça o nome de uma cidade
e diga se ela começa ou não com a palavra santo
"""
cidade = str(input('Escreva o nome da sua cidade ')).lower().strip()

print(f'A cidade de {cidade} começa com o nome de SANTO? {cidade[0:5] == "santo"}')