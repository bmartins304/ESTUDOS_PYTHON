lista = list()
posicao_maior = list()
posicao_menor = list()
maior = 0
menor = 0

for cont in range(0,5):
    lista.append(int(input('digite um valor: ')))

for i in range(0,len(lista)):
    if i == 0:
        maior = lista[i]
        menor = lista[i]
    if lista[i] >= maior:
        maior = lista[i]                           
    if lista[i] <= menor:
        menor = lista[i]

for p, x in enumerate(lista):
    if x == maior:
        posicao_maior.append(p)

for p, x in enumerate(lista):
    if x == menor:
        posicao_menor.append(p)

print(f'você digitou os valores {lista}')

print(f'o maior número nessa tupla é {maior} nas posições',end=' ')
for v in posicao_maior:
    print(v + 1,end='...')
print('')
print(f'o menor número nessa tupla é {menor} nas posições',end=' ')
for v in posicao_menor:
    print(v + 1,end='...')
print('')
print('fim')