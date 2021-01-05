"""
refaça o programa 35 

dizendo que se forma um triângulo 
equilatero todos os lados iguais
isósceles dois lados iguais 
escaleno todos os lados diferentes
"""

a = float(input('tamanho do segmento '))
b = float(input('tamanho do segmento '))
c = float(input('tamanho do segmento '))

if a+b > c and b+c > a and a+c > b:
   print('Formam um triângulo')
   if a == b == c:
      print('Forma um triângulo Equilátero') 
   elif a != b != c != a:
      print('Forma um triâgulo escaleno')    
   else:
       print('Forma um triângulo isósceles')
else:
   print('não formam um triângulo') 

