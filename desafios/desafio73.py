"""
Crie um programa que peça os 20 times
do campeonato brasileiro. Mostre
A) Os primeiros 5 colocados
B) Os 4 últimos
C) Uma lista em ordem alfabética
D) E a posição da Chapecoense
"""
clubes = ('Flamengo','Santos','Palmeiras','Grêmio','AthleticoPR',
'São Paulo','Internacional','Corinthians','Fortaleza','Goiás','Bahia','RB Brasil',
'Vasco','AtléticoMG','Fluminense','Botafogo','Ceará','Cruzeiro','Chapecoense','Avaí')
 

print(f"""
Os clubes do campeonato brasileiro {clubes}
Os cinco primeiros são:{clubes[:5]}
print(f'\nOs 4 últimos são {clubes[-4:]}
Os nomes dos clubes em ordem alfabética  {sorted(clubes)}
A O time da Chapecoense está na {clubes.index('Chapecoense')+1}° posição
""")