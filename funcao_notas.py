def notas(*num,sit=False):
    lista = [*num]
    dicinoario = dict()

    tot = maior = media = s = 0
    situacao = ''
    
    for x in lista:
        tot+=1
    dicinoario['total'] = tot
    for x in lista:
        if x > maior:
            maior = x
    dicinoario['maior'] = maior
    for x in lista:
        s += x
    media = s/len(lista)
    dicinoario['media'] = media
    if sit == True:
        if media >= 7:
            situacao = 'BOA'
        else:
            situacao = 'ruim'
    dicinoario['situação'] = situacao
    return dicinoario


resp = notas(5.5,2.5,1.5,sit=True)
print(resp)