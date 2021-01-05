"""
Faça um programa que leia vários produtos
e diga:
A) O total de preços dos produtos
B) Quantos produtos custam mais de R$ 1000 
C) O nome do produto mais barato
"""
mais_mil = 0
preco_mais_barato = 0
mais_barato = ''
total = 0
i = 0
while True:
    nome_produto = str(input('Escreva o nome do produto '))
    preco  = float(input('Escreva o preço do produto '))
    i += 1
    if i == 1 or preco < preco_mais_barato:
        preco_mais_barato = preco
        mais_barato = nome_produto
    if preco > 1000:
        mais_mil += 1
    
    total += preco
    parada = input('Quer para [S/n] ').lower()    
    if parada == 'n':
        break
print(f"""compra finalizada
R${total} foi o preço total dos produtos 
{mais_mil} foram o total de produtos que custam mais de 1000 reais
{mais_barato} foi o produto mais barato custando R${preco_mais_barato}
""")

    