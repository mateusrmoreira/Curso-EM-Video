"""
Escreva um programa que leia
uma frase e diga a primeira vez que aparece a letra A
Quantas vezes aparece a letra A e a última vez que aparece a letra A
"""
frase = str(input('Escreva uma frase ')).lower().strip()
print(f"""
A primeira letra A está em {frase.find('a')+1} 
A última letra A {frase.rfind('a')+1}
O total de vezes que aparece são {frase.count('a')}""")

