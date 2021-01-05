"""
Crie um programa que diga o aproveitamento
de um jogador de futebol.

Peça o nome: 
A quantidade de partidas jogadas:
Quantos gols foram marcados em cada partida:
A quantidade de gols: 
"""
total = 0
partidas = []
jogador = {}

jogador['nome']     = str(input('Coloque o nome do Jogador '))
jogador['partidas'] = int(input('Quantas partidas ele jogou? '))

for i in range(0, jogador['partidas']):
    g = int(input(f'quantos gols o jogador marcou na {i+1} partida?'))
    total += g
    partidas.append(g)
    
jogador['partidas'] = partidas[:]
jogador['total'] = total

print('-='*30,'\n',jogador,'\n','-='*30)

for k, v in jogador.items():
    print(f'O Campo {k} tem o valor de {v}')
print('-='*30)

print(f"""O jogador de nome {jogador["nome"]} Jogou {len(jogador["partidas"])} partidas E marcou {jogador['total']} gols""")
for i, v in enumerate(jogador['partidas']):
    print(f'  ==> Na partida {i+1} ele marcou {v} gols')
print(f'Foi um total de {jogador["total"]}')