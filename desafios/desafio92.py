"""
Crie um programa que leia Nome Ano de nasci-
mento e a carteira de trabalho e cadastre  -
(com a idade) a CT. Para as carteira de tra-
balho diferente de ZERO será pedido o salário 
e com quantos anos a pessoa vai se aposentar.
o ano de contratação. 
"""
from datetime import datetime

pessoa = dict()
pessoa['nome']         = str(input('Nome: '))
pessoa['nascimento']   = int(input('Ano de nascimento '))
pessoa['idade']   = datetime.now().year - pessoa['nascimento']
pessoa['ctps']         = int(input('Número da carteira de trabalho '))

if pessoa['ctps'] != 0:
    pessoa['ctps_ano'] = int(input('Em que ano assinou a carteira? '))
    pessoa['salario']  = float(input('Qual é seu salário? '))
    pessoa['aposentar_ano'] = (pessoa['ctps_ano']-pessoa['nascimento'])+35

print('-='*30)
print(f"""
-   Nome {pessoa['nome']}
-   Idade {pessoa['idade']}
-   CTPS N° {pessoa['ctps']}
-   Aposentadoria {pessoa['aposentar_ano']}""")