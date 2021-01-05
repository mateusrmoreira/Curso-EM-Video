"""
Crie um programa que peça uma expressão matemática
e verifique se os parênteses estão fechados corretammente
"""

expre = input('Digite uma expressão matemática ')
paren = []

for sim in expre:
    if sim == '(':
        paren.append(sim)
    elif sim == ')':
        paren.append(sim)
if len(paren) % 2 == 0:
    print('Expressão é válida')
else:
    print('Contém um erro na expressão ')