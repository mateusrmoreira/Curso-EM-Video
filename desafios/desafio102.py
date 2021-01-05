"""
Faça um programa que calcule o fatorial
a função fatorial recebe dois valores o
número, e o valor booleano, para o usuário
decidir se quer ou não ver o processo de f
atorial acontecer na tela.
"""

def factorial(num=1, show=False):
    """
    -> Calcula o fatorial de um número 
    :para num: O número que deve ser calculado
    :para show: A unidade que decide se quer ou não ver 
    o calculo
    """
    f = 1
    for i in range(num, 0, -1):
        if show:
            if i > 1:
              print(f'x {f}', end=' ', flush=True)
            else:
              print(f'= {f}', end=' ', flush=True) 
            f *= i                   
    return f

n = int(input('Escreva um número para ver seu factorial '))
sequencia = bool(input('Gostaría de ver a sequência? [ENTER PARA VER SOMENTE O RESULTADO] '))

print(f'\nO factorial de {n} é {factorial(n, sequencia)}')
