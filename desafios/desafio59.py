"""
Crie um programa que peça dois valores
e mostre um menu na tela
"""
menu = """
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] sair do programa
"""
n1, n2 = int(input('Escreva um número ')), int(input('Escreva um número '))
print(menu)
opcao = 0
while opcao != 5:
   print(menu) 
   opcao = int(input("\nQual é a sua opção? :> "))
   if opcao == 1:
      print(n1+n2)
   elif opcao == 2:
      print(n1*n2)       
   elif opcao == 3:
      if n1 > n2:
          print('O maior valor é ', n1) 
      else:
        print('O maior valor é ', n2)
   elif opcao == 4:
        print('Informe os números novamente')
        n1, n2 = int(input('Escreva um número ')), int(input('Escreva um número '))
   elif opcao == 5:
       print('Finalizando...')
   else:
       print('Ponha uma opção válida tente novamente')    
print('Fim do programa bye :) ')