total_gasto = 0
custa_mais_mil = 0
res = ''
produto_mais_barato = ''
mais_barato_preco = 0
count = 0
while True:
    count +=1
    res = ''
    produto = str(input('nome do produto: '))
    preco = float(input('qual o preço do produto: '))
    
    if count == 1:
         mais_barato_preco = preco
         produto_mais_barato = produto

    if preco < mais_barato_preco:
         mais_barato_preco = preco
         produto_mais_barato = produto

    total_gasto += preco

    if preco >= 1000:
         custa_mais_mil += 1

    
    
    while res != 'S' and res != 'N':
        res = str(input('quer continuar cadastrando os produtos?[S]/[N]')).upper()
    if res == 'N':
            break   
    
print(f'o total gasto na compra foi de R$ {total_gasto:.2f} reais.')
print(f'no total tem {custa_mais_mil} produtos custando mais de R$ 1000,00 reais.')
print(f'o produto com o preco mais barato foi {produto_mais_barato} de R${mais_barato_preco:.2f} reais.')
