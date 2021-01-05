from ext22 import moeda
n = int(input('Digite um preço: R$ '))

print(f"""
O aumento de {n} é {moeda.aumentar(n, 10)}
A dilução de {n} é {moeda.diminuir(n,10)}
O dobro de   {n} é  {moeda.dobro(n)}
 A metade de {n}  {moeda.metade(n)}""")
