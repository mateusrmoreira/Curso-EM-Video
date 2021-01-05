"""
 lendo o primeiro termo e a razão de uma PA, 
 mostrando os 10 primeiros termos da progressão 
 usando a estrutura while.
"""
print('   Gerador de P.A\n', '-='*10)


primeiro = int(input('Qual é o primeiro termo da progressão? '))
razao = int(input('Qual é a razão da progressão? '))
progressao = primeiro
i  = 1
while i < 10:
    print(f'{progressao} → ', end='')
    progressao += razao
    i+=1
print('FIM\n')