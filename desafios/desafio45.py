""" 25/03/2020 jan Mesu
Crie um programa que jogue jokenpô
"""
from time import sleep
from random import randint

arr = ['foo','Pedra', 'Papel', 'Tessoura']

computer = randint(1,3)

jokenpo = int(input("""
1 - Pedra

2 - Papel

3 - Tessoura

Escolha um # """))


winner = f'Você escolheu {arr[jokenpo]} e eu escolhi {arr[computer]} Ganhei'

if jokenpo == 1 and computer == 3:
   winner = f'Você escolheu {arr[jokenpo]} e eu escolhi {arr[computer]} você Ganhou'
elif jokenpo == 3 and computer == 2:
   winner = f'Você escolheu {arr[jokenpo]} e eu escolhi {arr[computer]} Ganhou'
elif jokenpo == computer:
    winner = f'Você escolheu {arr[jokenpo]} e eu escolhi {arr[computer]} empatamos'
sleep(1)
print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('Po')

print(winner)