"""
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, 
cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
"""

km = int(input('Distância da viagem ')) 
result = km*0.45 if km > 200 else km*0.50
print(f'O valor total da viagem foid e R${result:.2f}')