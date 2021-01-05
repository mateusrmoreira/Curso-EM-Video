"""
Crie uma função que meça os 
metros quadrados de um terreno
"""
def terreno(a,b):
    terreno = a*b
    print(f'O valor de {a}m x {b}m = {terreno:.2f}m²')


com = float(input('Comprimento em metros '))
al  = float(input('altura em metros '))

terreno(com,al)