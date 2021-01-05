"""
Crie uma função chama leiaint ele somente
Funciona parecido com aceita valores numéricos. 
o input mas não deixa os valores não númericos
passar
"""

def leiaint():
    num = input('Escreva um número decimal ')
    while num.isdecimal() == False:
        print('\033[0;31mErro esse valor não é válido\033[m')
        num = input('Escreva um número decimal ')
    num = int(num)
    return num

b = leiaint()

print(f'você acabou de digitar o número {b}')