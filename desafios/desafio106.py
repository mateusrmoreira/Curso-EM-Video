"""
Faça um mini-sistema com a ajuda do python o help()
uma função que peça um comando em python  ou biblo
teca e mostre a documentação
"""
c = (
    '\033[m',        # 0 - sem cores
    '\033[0;30;41m', # 1 - vermelho
    '\033[0;30;42m', # 2 - verde
    '\033[0;30;43m', # 3 - Amarelo
    '\033[0;30;44m', # 4 - Azul
    '\033[0;30;45m', # 5 - Roxo
    '\033[4;30m'    # 6 - Branco
);

def ajuda(com):
    titulo(f'acessando o manunal \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')

def titulo(msg,color=0):
    tam = len(msg) + 4
    print(c[color], end='')
    print('~'*tam)
    print(f'  {msg}  ')
    print('~'*tam)
    print(c[0], end='')


while True:
    titulo('SYSTEMA PYHELP', 1)
    comando = str(input('Função na biblioteca > '))
    if comando.lower() == 'fim':
        break
    else:
        ajuda(comando)


titulo('ATÉ LOGO', 1)  