""" 25/03/2020 jan Mesu
Escreva um programa para aprovar um empréstimo pré-aprovado
para a comprada de uma casa. O programa irá perguntar o valor da casa e o salário
de que está comprando e em quantos anos ele vai pagar o valor total.

O valor da parcela mensal não pode exceder o valor de 30%, SENÃO ele é negado.
"""

valorcasa = int(input('Digite aqui o valor da casa R$ '))
valorsalario = float(input('Digite aqui o valor mensal do salário R$ '))
anos = int(input('Quantos anos para pagar? '))
mensal = (valorcasa / (anos*12))
print(f'Proposta para casa de valor {valorcasa} para ser pago em {anos} anos a parcela ficaria de {mensal:.2f}.')
if mensal < valorsalario * (30/100):
   print(f'O crédito foi aprovado.') 
else:
   print('Infelizmente o crédito não pôde ser aprovado') 