brasil  = list()
estados = dict() 

for i in range(0,3):
    estados['uf']    = str(input('Escreva o nome da unidade federativa '))
    estados['sigla'] = str(input('Escreva a sigla da unidade federativa '))
    brasil.append(estados.copy())

for e in brasil:
    for k, v in e.items():
        print(f'{k} : {v}')