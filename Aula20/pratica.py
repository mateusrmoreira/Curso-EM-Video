def contador(*num):
    for i in num:
        print(f'{i}', end='→ ')
    print('FIM')

def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1
    print(lista)    

contador(1,2,3,5,6,2)
contador(1,2)
contador(1,2,9,6,3,2,4,24,6,7,3234,2)

dobra([1,2,3,5,6,2])