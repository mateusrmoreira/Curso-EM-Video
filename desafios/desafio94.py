"""
Crie um programa que leia
nome, idade, sexo de várias pessoas
guardando tudo em um dicionário e to-
dos
os dicionários dentro de uma lista. No 
final mostre 

A) Quantas pessoas foram cadastrad-
as
B) Média de idade do grupo
C) A lista com todas as mais velhas
D) A lista com todas as pessoas c-
om a idade acima da média
"""
pessoasMulherList = list()
pessoasMedia = dict()
pessoasMediaList = list()
pessoa = dict()
registro = list()
media = soma = cadastradas = 0

while True:
    pessoa['nome']  = input('Digite o nome da pessoa ')
    pessoa['idade'] = float(input('Digite sua idade '))
    soma += pessoa['idade']
    pessoa['sexo']  = input('Digite seu sexo [M/F] ')
    
    while pessoa['sexo'] not in 'MFmf' or pessoa['sexo'] == '':
        pessoa['sexo']  = input('Digite seu sexo [M/F] ')  
    
    cadastradas += 1
    registro.append(pessoa.copy())
    
    resp = input('Quer continuar? [S/N] ').lower()
    if resp == 'n':
        break

media = soma / len(registro)

for i, value in enumerate(registro):
    print('-='*15)
    for k, v in value.items():
        print(f'{k}: {v}')
        if k == 'idade' and v > media:
           pessoasMedia = {'nome':    value['nome'], 
                            'sexo':   value['sexo'], 
                            'idedae': value['idade']}
           pessoasMediaList.append(pessoasMedia.copy())
        elif k == 'sexo' and v in 'Ff':
           pessoasMulherList.append(value['nome'])
print('-='*15) 
print('Todas as mulheres cadastradas foram')
for i in pessoasMulherList:
    print(i, end=' ')

print('\n','-='*15)       
print(f'Foram Cadastradas um total de {cadastradas} Pessoas\nA média de idades é {media:.2f}\n')
print('-='*15)

print(' Pessoas acima da média de idade\n', '-='*15)
for i in pessoasMediaList:
    for k, v in i.items():
        print(f'{k}: {v}')