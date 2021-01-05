"""
Escreva um programa com o nome de maior
ele será capaz de ler vários valores e dizer o meior
"""

from time import sleep

def maior(*num):

    print('-='*10)
    maior = total = 0

    for v in num:
        print(v, end=' ',flush=True)
        sleep(0.1)
        if v > maior or total == 0:
            maior = v
      
        total += 1
    print(f'\nForam um total de {total} números e o maior deles é {maior}')


maior(10,234,13423,13466,112,123)
maior(1,2)
maior(0)
maior(-0.12323223,-1,-2,-3,-4,-5)
