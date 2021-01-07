def aumentar(valor, porcentagem): 
    
    valor += (valor *(porcentagem/100))
    return valor

def diminuir(valor, porcentagem):
    valor -= (valor *(porcentagem/100))
    return valor

def dobro(valor):
    return valor * 2


def metade(valor):
    return valor / 2

def moeda(valor, porcentagem):
    valor_dobro    = dobro(valor)
    valor_diminuir = diminuir(valor, porcentagem)
    valor_aumento  = aumentar(valor, porcentagem)
    valor_metade   =  metade(valor)
    result = f"""
--------------------------------------------
          VALORES FORMATADOS
--------------------------------------------
  O dobro de {valor:.2f}  R$ {valor_dobro}
  A metade de {valor:.2f} R$ {valor_metade}
---------------------------------------------
  O diminuir de {porcentagem}% de {valor:.2f} ficará R$ {valor_diminuir}
  O aumento {porcentagem}% de {valor:.2f} ficará R$ {valor_aumento}
---------------------------------------------
"""
    return result.replace('.', ',')

