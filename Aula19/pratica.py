pessoas = {'nome':'Gustavo', 'sexo': 'M', 'idade':26}
print(f'O {pessoas["nome"]} {pessoas["sexo"]} Tem {pessoas["idade"]}')
del pessoas['sexo']
pessoas['peso'] = 90
for v, k in pessoas.items():
    print(f'{v} = {k}')