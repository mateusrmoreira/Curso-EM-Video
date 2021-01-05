def fatorial(num):
    f = 1
    for i in range(1,num+1):
        f *= i
    return f

num = int(input('Digite um valor :> '))
print(f'O fatoriala de {num} é {fatorial(num)}')
