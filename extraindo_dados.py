lista = list()
cont = 0
while True:
    n = int(input('insira um valor: '))
    cont+=1
    lista.append(n)
    resp = str(input('quer continuar digitando? [S]/[N]')).upper()
    if resp == 'N':
        break

lista.sort(reverse=True)
print(f'você digitou {cont} elementos')
print(lista)
if 5 in lista:
    print('o número 5 esta na lista')
else:
    print('o número 5 não está na lista.')