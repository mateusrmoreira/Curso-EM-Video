"""
Crie um programa que pergunte
a IDADE e o SEXO de cada pessoa
no final ele mostrará
A) quantas pessoas tem mais de 18 anos
B) quantos homens foram cadastrados
C) quantas mulheres +20 foram cadastradas
"""
homem_contador   = 0
mulher_contador  = 0
pessoa_contador  = 0
sexo = ''

while True:
    print('Cadastro Nacional de Pessoa burra')
    idade = float(input('Qual é sua idade? '))
    while True:
        sexo  = str(input('Qual é seu sexo? [M/F]')).lower().strip()
        if sexo[0] in 'fm':
            break

    if sexo == 'f' and idade <= 19:
       mulher_contador += 1
    if sexo == 'm':
        homem_contador += 1
    pessoa_contador += 1
    
    resp = str(input('Quer continuar? [S/n] ')).lower()
    if resp == 'n':
        break


print(f""" Cadastro nacional de Pessoas Burras 
foram cadastradas um total de:
{pessoa_contador} Pessoas cadastradas
{homem_contador} Homens burros
{mulher_contador} Mulheres burras com menos 20 anos
""")

