c = 0

def contador(i, f, p):
    """
    Contador conta de um numero dado como inicio ate o numero final
    Para i: inicio da contagem
    Para f: final da contagem
    Para p: passos da contagem
    return: sem retorno
    """
    global c
    if p < 0:
        p*=-1
    c = i
    if i <= f:
      while c <= f:
         print(c, end='', flush=True)
         c += p
    else:
      while c >= f:
         print(c, end='', flush=True)
         c -= p
print(contador(10,100,1))
print(contador(100,10,1))

help(contador)