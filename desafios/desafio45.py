"""
Creating a program that implements a jokenpo game
"""

from random import randint

prompt = """
=============
To Play JOKENPO you need yo write down one of these numbers

[0] Rock

[1] Papper

[2] Scissors 

=============

console ~$ """

player  = int(input(prompt))

while player > 2:
    print('Make sure you write the correct number')
    player = int(input(prompt))

randomly = randint(0,2)

computer = ['Rock', 'Papper', 'Scissors']

result  = computer[randomly]

winner = 'You are the winner'

if result == computer[player]:
   winner = f'Computer put {result} you put {computer[player]} it is a draw' 
elif result == 'Papper' and computer[player] == 'Rock':
   winner = f'Computer put {result} you put {computer[player]} computer wins'
elif  result == 'Rock'   and computer[player] == 'Scissors':
   winner = f'Computer put {result} you put {computer[player]} computer wins'
elif  result == 'Scissors' and computer[player] == 'Papper':
   winner = f'Computer put {result} you put {computer[player]} computer wins'


print(winner)
