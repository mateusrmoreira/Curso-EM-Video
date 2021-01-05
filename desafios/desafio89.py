"""
Crie um programa que leia o nome e duas notas
de vários alunos e no final mostre o boletim
contendo a média de cada aluno individualmente  
"""

medias = 0
alunos = list()
individuo = list()

while True:
    """
    Aqui inicia o cadastro do aluno a primeira parte é pedido o nome 
    n1 e n2 corresponde as notas do semestre
    medias fazem todas as médias e acrescenta como um 3° elemento
    """
    individuo.append(input('Nome do aluno '))
    
    n1 = float(input('Nota do Aluno 1° Semestre '))
    n2 = float(input('Nota do Aluno 2° Semestre '))
    
    individuo.append(n1)
    individuo.append(n2)
    medias = (n1+n2) / 2
    individuo.append(medias)

    alunos.append(individuo[:])
    individuo.clear() 
    continuar = input('Deseja continuar? [Y/n]')
    if 'n' in continuar:
        break


print(f'No.      Nome         Média\n')
for i in range(0, len(alunos)):
   print(f'{i}{alunos[i][0]:^20} {alunos[i][3]}')

quest = int(input('Qual aluno você gostaría de ver as notas? 999 para sair '))      
for i in alunos:
    while quest != 999:
        while quest > len(alunos):
           quest = int(input('Número acima de alunos cadastrados\ntente novamente 999 para sair '))
        print(f"""\n\nN0: {alunos[quest][0]} Nome {alunos[quest][1]}
1° Semestre {alunos[quest][1]} 2° Semestre {alunos[quest][1]} Média {alunos[quest][3]}""")   
        quest = int(input('Qual aluno você gostaría de ver as notas? 999 para sair '))   