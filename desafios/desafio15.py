""" 15/03/2020 by jan Mesu
 Crie um programa para gerenciar um aluguel de carro.
Calcule o preço do aluguel baseado na quantidade de dias R$60 P/ dia
e nos quilômetros rodados R$0.15 p/ Quilômetro.
"""

dias        = int(input('Quantos dias o carro ficou alugado?  '))
quilometros = float(input('Quantos quilômetros foram rodados? '))

print(f"""\nO carro foi alugado por {dias} dias pagando o preço de R$60 por dia 
Com {quilometros} quilometros rodados com R$0.15 por quilômetro
Tudo dá um total de R$ {dias*60+quilometros*0.15:.2f} A Pagar    
""")