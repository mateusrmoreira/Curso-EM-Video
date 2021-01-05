"""
Crie um programa que peça um valor em metros
e mostre esse valor em centímetros e milimetros

Com o Guanabara fizemos do Quilômetros, Hectometros, Decametros
"""

metros = int(input('Escreva um valor em metros [M] '))

print(f"""
{metros} Metros são 
Quilometros {metros / 1000}km
Hectometros {metros / 100}hm
Decametros  {metros / 10}dam
Decimetros  {metros * 10} Dcm
Centímetros {metros * 100}cm
Milímetros {metros * 1000}mm
""")