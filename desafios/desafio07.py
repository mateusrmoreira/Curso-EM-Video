"""
Leia um programa que peça duas notas de um aluno
e mostre sua média
"""

n1, n2 = float(input('Informe a nota do primeiro semestre ')), float(input('Informe a nota do segundo semestre '))

print(f"""
A nota do primeiro semestre {n1}
A nota do segundo semestre {n2}
Média final {(n1+n2)/2:.1f}
""")