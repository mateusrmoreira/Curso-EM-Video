""" 16/03/2020 jan Mesu
Faça um programa que leia uma frase e diga
quantas vezes aparece a letra A
em que posição ela aparece na primeira vez
em que posição ela aparece na última vez
"""
frase = str(input('Escreva uma frase :> ')).strip().lower()
print(f""""A letra A aparece {frase.count('a')} Vezes 
A primeira vez que aparece é na posição {frase.find('a')+1}
E a última vez que aparece é na posição {frase.rfind('a')}
""")