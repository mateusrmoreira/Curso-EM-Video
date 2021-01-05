""" 18/03/2020 jan Mesu
Faça um programa que leia a velocidade de um carro 
se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi 
multado. A multa vai custar R$ 7,00 por quilômetro últrapassado.
"""

speed = int(input('Digite a velocidade do carro KM/H '))

if (speed - 80) > 0:
    print(f"""Você passou em uma velocidade de {speed} em uma pista de 80KM/H
Você pagará uma multa de R$ {(speed - 80)*7:.2f}
""")
print('Tenha um bom dia, Dirija com segurança') 