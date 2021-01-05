"""
"""
numero = int(input('Digite um número para ver sua tabuada '))
i = 1

while True:
    if numero < 0:
       break
    print(f'{numero} x {i:<2} = {numero*i}')
    i+=1
    if i > 10:
        numero = int(input("""
SE quiser continuar digite um número positivo
SE Não um número negativo """)) 
        i = 1

