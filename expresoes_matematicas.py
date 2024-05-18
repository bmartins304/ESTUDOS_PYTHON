cont = 0
exprecao = str(input('digite a expreção numerica -> '))
lista = exprecao[:]
if '(' not in lista:
    print('expreção sem pareteses')
else:
    for x in lista:
        if x == '(' or x == ')':
            cont+=1
if cont % 2 == 0:
    print('a expreção é valida!')
else:
    print('a expreção está errada!')
