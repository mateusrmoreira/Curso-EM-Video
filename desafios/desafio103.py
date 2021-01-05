"""
Crie um programa chamado ficha que receba dois parâmetros opc
ionais, um o nome e outro quantos gols ele marcou. Se não for 
recebido nenhum valor o programa deverá retornar <Jodagor des
conhecido> ou 0 gols
"""

def ficha(nome='', gols=0):
     
    if nome == '':
        nome = '<Desconhecido>'
    
    print(f' O Jogador {nome} fez {gols} gols no campeonato')

n = input('Qual é o nome do jogador? ').lower().strip()
g = input('Quantos gols ele marcou? ').lower().strip()


if g.isnumeric():
    g = int(g)
else:
    g = 0

if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)

