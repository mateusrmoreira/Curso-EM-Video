"""
Elabore um programa que calcule o valor a ser pago
por um produto considerando seu preço normal
e a condição de pagamento 

Á vista dinheiro/cheque 10% de desconto 

a vista cartão 5% de desconto 

em até 2 vezes no cartão preço normal

3x ou mais no cartão 20% de juros
"""

formas = """ Qual é a forma de pagamento?
[0] Á vista dinheiro/cheque 10% de desconto 

[1] a vista cartão 5% de desconto 

[2] em até 2 vezes no cartão preço normal

[3] 3x ou mais no cartão 20% de juros
"""
prompt = int(input(formas))

valor = float(input('Preço do produto '))

result = valor

if prompt == 0:
   result =  valor - (valor * 0.10)
elif prompt == 1:
   result =  valor - (valor * 0.05) 
elif prompt == 3:
     result =  valor + (valor * 0.20)
print(f'O valor total do produto é {result}')