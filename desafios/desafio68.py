"""
Faça um programa que jogue par ou impar
o programa finaliza quando o jogador perder
e mostra a sequência de vitórias consecutivas
"""
from random import randint

print('-='*20,f'\n      Vamos jogar PAR OU ÍMPAR\n', '-='*20)

i = 0
while True:

    computer = randint(0,10)
    jogador = int(input('Digite um número entre 0 e 10 '))
    play    = computer + jogador
    escolha = str(input('Escolha par ou ímpar [P/I] ')).lower()
    
    print(f'O computador jogou {computer} você jogou {jogador} a soma é {play}')
    
    if play % 2 != 0 and escolha == 'p' or play % 2 == 0 and escolha == 'i':
        break 
    i += 1
print(f'você teve {i} vitórias consecutivas')



        

