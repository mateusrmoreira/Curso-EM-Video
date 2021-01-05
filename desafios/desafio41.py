"""
A condeferaçãod de natação
precisa de um programa para categorías

até 9 anos é mirim
até 14 anos infantil 
até 19 junior
até 20 sênior
acima de 25 é master
"""

idade = int(input('Qual é a idade do nadador? '))
status = 'Infantil'
if idade < 9:
   status = 'Mirim' 
elif idade > 14 and idade <= 19:    
    status = 'Junior'
elif idade >= 20 and idade < 25:
    status = 'Sênior'
elif idade > 24:
    status = 'Master'    
print(f'O nadador está na categoria {status}')    