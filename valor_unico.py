lista= list()
while True:
    n = int(input('digite um valor: '))
    if n not in lista:
        lista.append(n)
    else:
        print('número duplicado.')
    resp = str(input('você quer continuar adicionando? [S]/[N]')).upper() 
    if resp == 'N' :
        break
lista.sort()
print(lista) 
