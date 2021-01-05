"""
Desenvolva um programa
para calcular o imc de uma pessoa e mostre o resultado

abaixo de 18.5 : Abaixo do peso
entre 18.5 e 25 peso ideal
de 25 até 30 sobrepeso
30 até 40 obesidade
aciam de 40 obesidade mórbda
"""

peso = float(input('Escreva seu peso '))
altura = float(input('Escreva sua altura '))
imc  = peso / altura**2

status = f'o IMC de {imc:.2f} Peso ideal'

if imc < 18.5:
   status = f'o IMC de {imc:.2f} abaixo do Peso' 
elif imc > 25 and imc < 30:
    status = f'o IMC de {imc:.2f} Sobrepeso'
elif imc <= 40 and imc > 30:
    status = f'o IMC de {imc:.2f} Obeso'
elif imc > 40:
    status = f'o IMC de {imc:.2f} Obesidade Mórbida'
print(status)