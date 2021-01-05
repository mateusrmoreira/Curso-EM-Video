"""
Faça um programa que calcule a méda de duas
notas de um aluno.

se abaixo de 5.0 ele foi reprovado
se entre 5.0 e 6.9 ele está em recuperação
acima de 7.0 aprovado
"""
status = 'Recuperação'
media1 = float(input('Nota do primeiro semestre '))
media2 = float(input('Nota do segundo semestre '))

if (media1+media2)/2 > 7.0:
    status = 'Aprovado'
elif (media1+media2)/2 < 5.0:
    status = 'Reprovado'     
print(f"""
As notas {media1} do primeiro semestre
E {media2} do segundo semestre somam uma média geral e 
{(media1+media2)/2} pontos o aluno está {status}
""")