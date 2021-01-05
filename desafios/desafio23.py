"""
Faça um programa que leia um número de 0
a 9999 e mostre sua unidade dezena centena e milhar
"""
numero = int(input('escreva um número entre 0 e 9999 '))

print(f"""
 Existem:
  {numero//1000%10} Milhares
  {numero//100%10} Centenas
  {numero//10%10} Dezenas
  {numero//1%10} Unidades
"""
)