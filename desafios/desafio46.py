"""
Faça um programa que mostre na tela uma
contagem regressiva. e no final solte 
fogos de artifício
"""
from emoji import emojize
from time  import sleep
for i in range(10,1,-1):
    print(i)
    sleep(0.5)
print(emojize(':fireworks:'))