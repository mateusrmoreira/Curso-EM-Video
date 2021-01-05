"""
Receba o nome de uma pessoa
mostre todas as letra maúsculas
todas as letras minúsculas
quantas letras tem ao todo sem espaços
quantas letras tem o primeiro nome
"""
nome = str(input('Escreva seu nome completo '))

print(f"""
O nome com todas as letras maiúsculas {nome.upper()}
O nome com todas as letras minúsculas {nome.lower()}
O nome sem espaços {nome.replace(" ", "")}
Seu nome tem ao todo {len(nome) - nome.count(' ')}
Quantas letras tem o primeiro nome {nome.find(' ')}
""")