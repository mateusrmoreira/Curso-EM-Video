""" 18/03/2020 jan Mesu
 Faça um programa crie o orçamento de uma viagem
ele pede a distância em km, cobrando R$ 0,50 centavos por quilômetro 
em viagens de até 200 KM e viagens mais longas cobra R$ 0,45
"""
km = int(input('Escreva a distância em quilômetros '))
fee = km * 0.5
if km > 200:
   fee = km * 0.45
result = f'O preço total da viagem foi R$ {fee}'
print(result)