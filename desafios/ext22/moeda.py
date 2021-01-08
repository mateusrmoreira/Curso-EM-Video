def aumentar(valor, porcentagem=0, formatado=False): 
    valor += (valor *(porcentagem/100))
    return valor if formatado == False else moeda(valor)

def diminuir(valor, porcentagem=0, formatado=False):
    valor -= (valor *(porcentagem/100))
    return valor

def dobro(valor, formatado=False):
    valor *= 2
    return valor if formatado == False else moeda(valor)


def metade(valor, formatado=False):
    valor /= 2
    return valor if formatado == False else moeda(valor)

def moeda(valor, moeda='R$'):
    result = f'O {moeda} {valor:>.2f} Total'
    return result.replace('.', ',')

