""" 25/03/2020 jan Mesu

Escreva um programa que peça um número inteiro qualquer
e peça para o usuário escrever uma base de conversão.

[1] Converter para Binários
[2] Converter para octal
[3] Converter para hexadecimal
"""

select = int(input("""
Escolha uma base numéria para conversão

1 - Para binários

2 - Para octal

3 - Para Hexadecimal

        Escolha um número # """))

answer = int(input('Escreva um número para converter na base escolhida $ '))


if select == 1:
   answer = bin(answer)
elif select == 2:
   answer = oct(answer)
elif select == 3:
   answer = hex(answer)    
elif select > 3:
   print('Opção inválida tente novamente ')

print(answer)
