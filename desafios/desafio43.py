""" 25/03/2020 jan Mesu
Desenvolva uma lógica que peça o peso de uma pessoa e diga o status de acordo com a tabela abeixo

Abaixo de 18.5 Abaixo do Peso
Entre 18.5 e 25 peso ideal
entre 25 e 30 sobre peso
entre 30 até 40 Obesidade
acima de 40 obesidade mórbida
"""

altura = float(input('Digite a sua altura '))
peso = float(input('Digite o seu peso '))
imc = peso / (altura*altura)

result = 'Sobre Peso'

if imc <= 18.4:
   result = 'Abaixo do peso' 
elif imc >= 18.5 and imc <= 25:
   result = 'Peso ideal' 
elif imc >= 30 and imc <= 39:
    result = 'Obesidade'
elif imc >= 40:
    result = 'Obesidade Mórbida'
print(f'O imc é de {imc:.2f} e o resultado é {result}')