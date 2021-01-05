"""
Escreva um programa que leia um número N inteiro qualquer e 
mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
"""

termos = int(input('Quantos termos você quer ver da sequência de Fibonacci? '))
fib1 = 0
fib2 = 1
i = 0
print(f'F{i} = {fib1}')
i += 1
while i <= termos:
     fib1, fib2 = fib2, fib2+fib1
     print(f'F{i} = {fib1} ')
     i+=1
print('FIM')
