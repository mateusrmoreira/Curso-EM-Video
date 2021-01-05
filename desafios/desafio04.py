""" Faça um programa que leia algo pelo teclado
e mostre na tela o tipo primitivo e todas
as informações possíveis
"""

word = input('Digite qualquer coisa ~$ ')

print(f"""
Tipo {type(word)}
Alpha Numerico {word.isalnum()}
Numérico {word.isnumeric()}
Alfa  {word.isalpha()}
Decimal {word.isdecimal()}
Identificador {word.isidentifier()}
Printável {word.isprintable()}
Está em minuscula {word.islower()}
é um espaço {word.isspace()}
É um dígito {word.isdigit()}
Está em letra maiúscula {word.isupper()}
""")
