"""
Faça um programa que tenha uma função  chamada
contador() com parâmetros de inicio, passo e fim
seu programa tem que realizar trÊs contagens
de 1 até 10, de 10 até 1 e uma que o usuário decide
"""
from time import sleep

def verificador(p):
    if p == 0:
        p = 1
    elif p < 0:
        p *= -1
    return p

def contador(i, f, p):
    p = verificador(p)

    print('-='*10)
    print(f'Contar de {i} para {f} de {p}')

    c = i
    if i < f:
      while c < f:
          print(c, end=' ', flush=True)
          sleep(0.1)
          c+=1
    else:      
        while c > f:
            sleep(0.1)
            print(c, end=' ', flush=True)
            c-=p
    print()

contador(1,10,1)
contador(10,0,1)

inicio = int(input('Escreva o valor do inicio '))
fim      = int(input('Escreva o valor do fim '))
passo  = int(input('Escreva o valor do passo '))
contador(inicio, fim, passo)
