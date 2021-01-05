"""
Escreva um programa que leia a velocidade de um carro
Se ele ultrapassar 80 km/h receberá uma multa de R$7,00 por km
"""
velocidade = int(input('Digite a velocidade do carro '))
resultado = 'Dirigja com cuidado'
if velocidade > 80:
   resultado = f"""
   Você excedeu a velocidade limite em {velocidade - 80}KM pagará uma multa de R${(velocidade - 80) * 7}
   """
print(resultado) 