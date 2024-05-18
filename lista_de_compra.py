lista_compra = ('lápis',1.75,'borracha',2.00,'caderno',15.90,'estojo',25.00
                ,'transferidor',4.20,'compasso',9.99,'mochila',120.30,'canetas'
                ,22.30,'livro',34.90)
preco = lista_compra[1::2]
objetos = lista_compra[0::2]
print('='*40)
print(f'{'LISTA DE COMPRAS':^40}')
print('='*40)
for c in range(0,len(lista_compra)//2):
    print(f'{objetos[c]:-<30}',f'R$ {preco[c]}')
print('='*40)