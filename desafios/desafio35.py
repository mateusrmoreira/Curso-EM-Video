"""
Desenvolva um programa 
que leia um comprimento de 3 retas e diga se elas formam
um triângulo 
"""

a = float(input('tamanho do segmento '))
b = float(input('tamanho do segmento '))
c = float(input('tamanho do segmento '))

if a+b > c and b+c > a and a+c > b:
   print('Formam um triângulo') 
else:
   print('não formam um triângulo') 

