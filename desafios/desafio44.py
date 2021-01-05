""" 25/03/2020 jan Mesu
elabore um programa que calcule o valor a ser pago por um produto consideranço seu preço normal
preço e condição de pagamento

- À vista no dinheiro / Cheque 10% de desconto

- À vista no cartão 5% de desconto

- Em até 2x no cartão preço normal

- 3 ou mais vezes no cartão vai com 20% de juros
"""

preco = int(input('Digite o preço do produto R$ '))

menu = int(input("""

1 - À vista no dinheiro / Cheque 10% de desconto

2 - À vista no cartão 5% de desconto

3 - Em até 2x no cartão preço normal

4 - 3 ou mais vezes no cartão vai com 20% de juros

Escolha a forma de pagamento   # """))

total = preco - (preco * (10/100))

if menu == 2:
    total = preco - (preco * (5/100))
elif menu == 3:
    total = preco
elif menu == 4:
    total = preco + (preco * (10/100))

print(f'O valor da conta é R$ {preco} com a forma de pagamento o valor total ficará R$ {total}')