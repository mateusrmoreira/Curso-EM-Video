"""
 lendo o primeiro termo e a razão de uma PA, 
 mostrando os 10 primeiros termos da progressão 
 usando a estrutura while. E peça se a pessoa 
 quer ver mais termos
"""
print('   Gerador de P.A\n', '-='*10)


primeiro = int(input('Qual é o primeiro termo da progressão? '))
razao = int(input('Qual é a razão da progressão? '))
progressao = primeiro
i  = 1
while i != 0:
    print(f'{progressao} → ', end='')
    progressao += razao
    i+=1
    if i == 10:
       i = int(input('\nQuantos termos mais você gostaría de ver? ')) 
print('FIM\n')