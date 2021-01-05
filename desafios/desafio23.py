""" 16/03/2020 jan Mesu
Faça um programa que conte um número de 0 a 999
e mostre na tela separados as unidades, as dezenas, centenas e milhar

Exemplo 1834

Unidade 4
Dezena  3
centena 8
Milhar  1
"""
numero = int(input('Digite um número entre 0-9999 :> '))


print(f"""O número digitado foi {numero} ele tem
Unidade {numero   // 1 %10}
Dezena  {numero  // 10 %10}
Centena {numero // 100 %10}
Milhar  {numero // 1000 %10}
""")

