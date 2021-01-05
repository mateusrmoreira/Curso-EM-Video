nome = str(input('Qual é seu nome? ')).title()

if nome == 'Mateus':
   print('Que nome bonito você tem!') 
elif nome == 'Piter' or nome == 'Mat' or nome == 'Hélio':
   print('Seu nome é bem normal aqui no brasil') 
else:
   print('Tudo bem! ') 
print(f'tenha um bom dia {nome}')