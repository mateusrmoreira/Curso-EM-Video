"""
Crie um programa que o usuário possa digitar
sete valores numéricos e cadastreas em uma -
única lista que mantenha separados os valores
ímpares e pares no final mostre os valores p-
ares e ímpares em ordem crescente.
"""
impar = list()
par = list()
listão = list()

for i in range(0,7):
    n = int(input('Escreva um número '))
    if n % 2 == 0:
        par.append(n)
        listão.append(par)
    else:
        impar.append(n)
        listão.append(impar)   
impar.sort()
par.sort()
print(f'Lista com números pares {par}\nLista com números ímpares {impar}')
    


