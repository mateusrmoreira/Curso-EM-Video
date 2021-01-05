"""
Melhore o jogo do desafio 28
o computador vai pensar um número
e só termina quando o usuário acerta
no final mostra a quantidade de palpites
"""

from random import randint
from time import sleep
computador = randint(0,10)
user =  int(input('Escreva um número entre 0, 10 '))
count = 0
while user != computador:
   if user > computador:
      user =  int(input('Menos, escreva um número entre 0, 10 '))
   elif user < computador:
      user =  int(input('Mais, escreva um número entre 0, 10 '))
   count +=1

winner = f'O computador colocou o número {computador} e você colocou {user} você acertou'
print(winner, f'{count} tentativas')