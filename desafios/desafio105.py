"""
Faça um programa que leia várias notas de um aluno
e um parâmetro opcional booleano ao qual mostre
se a situação das notas são boas, razoáveis ou
ruims Coloque tudo dentro de dicionário. com as
chaves, total de notas, média, maior nota, menor
nota e situaçao
"""

def notas(*num, cond=False):
    aluno = dict()
    aluno['total'] = len(num)
    aluno['maiornota'] = max(num)
    aluno['manornota'] = min(num)
    aluno['media'] =  sum(num) / len(num)
    if cond == True:
        if aluno['media'] < 6:
            aluno['situacao'] = 'REPROVADO'
        elif aluno['media']  < 7:
            aluno['situacao'] = 'RECUPERAÇÃO'
        else:
            aluno['situacao'] = 'APROVADO'
    return aluno      


aluno_notas = notas(0,10, cond=True)

print(aluno_notas)