from ext22 import moeda
n = int(input('Qual o valor que você gostaría de ver? '))
print(f"""
O aumento de {n} é {moeda.aumentar(n, 10, True)}
A dilução de {n} é {moeda.diminuir(n,10, True)}
O dobro de   {n} é {moeda.dobro(n, True)}
A metade de {n}  é {moeda.metade(n, True)}""")