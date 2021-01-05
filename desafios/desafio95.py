"""
Aprimore o exercício 93
agora recebendo detalhes de 
vários jogadores e dando detalhes
de aproveitamento de cada um deles
"""

total = 0
partidas = []
time = []
jogador = {}
resp = ''
p = 0 
while resp != 'n':
    jogador['nome']     = str(input('Coloque o nome do Jogador '))
    jogador['partidas'] = int(input('Quantas partidas ele jogou? '))
    for i in range(0, jogador['partidas']):
        g = int(input(f'quantos gols o jogador marcou na {i+1} partida? '))
        total += g
        partidas.append(g)
    resp = str(input('Quer continuar? [S/N]')).lower()
        
    jogador['partidas'] = partidas[:]
    jogador['total'] = total
    time.append(jogador.copy())
    total = 0
    partidas.clear()
    jogador.clear()

for k, v in enumerate(time):
    print(f'{k}: {v["nome"]} {v["total"]} gols')

while True:
   
    n = int(input('Digite o número do jogador que você quer ver '))
    while n > len(time) or n < 0:
       n = int(input('Erro número acima de jogadores cadastrados tente novamente '))
    
    print(f'Jogador {time[n]["nome"]}')
    for k in time[n]['partidas']:
        p+=1
        print(f'Na partida {p} O jogador Marcou {k} Gols')
           
    p = 0
    print(f'Foi um total de {time[n]["total"]}')

    resp = int(input('Quer var mais um jogador? [999] para sair '))
    if resp == 999:
        break