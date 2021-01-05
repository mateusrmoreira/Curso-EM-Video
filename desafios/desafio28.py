"""
Faça o computador advinhar o número escolhido pelo computador entre
0 e 5 o programa diz quem venceu
"""
from random import randint
from time import sleep
computador = randint(0,5)
user =  int(input('Escreva um número entre 0, 5 '))
print('Processando')
sleep(3)

winner = f'O computador colocou o número {computador} e você colocou {user} O computador venceu'

if user == computador:
   winner = f'O computador colocou o número {computador} e você colocou {user} você venceu'

print(winner)