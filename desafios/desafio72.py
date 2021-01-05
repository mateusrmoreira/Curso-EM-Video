"""
Peça o usuário para digitar um número entre 0 e 20
e mostre o valor do número por extenso
"""
extenso = ("zero","um","dois","três","quatro","cinco","seis","sete",
            "oito","nove","dez","onze","doze","treze","catorze", "quize",
            "dezesseis","dezesete","dezoito","dezenove","vinte")
while True:
    numero = int(input('Digite um número entre 0 e 20 '))
    
    if numero >= 20 or numero <  0:
       numero = int(input('Número inválido digite um número entre 0 e 20 '))
    else:
       print(f'O número digitado foi o número {extenso[numero]}')  
    
    continuar = str(input('Quer continuar? [S/n] ')).lower()
    if continuar == 'n':
        break