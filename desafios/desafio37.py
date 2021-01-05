"""
Escreva um programa que leia 
um número inteiro e converta par outras bases numéricas

1 para binário 
2 para octal
3 para hexadecimal
"""
prompt  = """ Para converter para 
Binário digite 1 
Octal digite   2
Hexadecimal    3
"""
console = input(prompt)
numero  = int(input('Escreva o número para ser feita a conversão '))
result = bin(numero)
if console == 2:
   result =  oct(numero)
elif console == 3:
   result = hex(numero) 
print(f'O resultado é {result}')