""" 16/03/2020 jan Mesu
Crie um programa que leia o nome completo de uma pessoa

O nome com todas as letras maiúsculas
O nome com todas as letras minúsculas
Conte todas as letras sem considerar os espaços
Quano quantas letras tem o primeiro nome
"""

nome = str(input('Escreva seu nome completo ')).strip()

print(f"""
O seu nome é {nome}
O seu nome com letras maiúsculas fica {nome.upper()}
O seu nome com letras minúsculas fica {nome.lower()}
O total de letras do seu nome tem {nome.find(' ')} letras
O total de letras do seu primeiro nome {len(nome.split()[0])}
""")