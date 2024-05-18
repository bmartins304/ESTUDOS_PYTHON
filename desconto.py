preco = float(input('qual o preço do produto? '))
desc = preco*(5/100)
descR = preco - desc
print('R$ {} reais com 5 por cento de desconto ficará, R$ {:.2f} reais'.format(preco,descR))