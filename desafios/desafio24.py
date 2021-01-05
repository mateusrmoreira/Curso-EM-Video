""" 16/03/2020 jan Mesu
Crie uma programa que peça o nome de uma cidade
e diga se a cidade começa ou não com a palavra SANTO
"""
cidade = str(input('Escreva o nome da sua cidade :> ')).strip().upper()
santo  = cidade[:6]
print(f'Tem santo no nome da cidade? {"SANTO " in santo}')