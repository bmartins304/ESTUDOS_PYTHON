import os

matriz = list()
vetor = list()
soma = soma_segunda_coluna= maior_valor = 0

for x in range(0,3):
    for y in range(0,3):
        vetor.append(int(input(f'insira um valor para {x,y}: ')))
    matriz.append(vetor[:])
    vetor.clear()

os.system('cls') or None
for x in range(0,len(matriz)):
    for y in range(0,len(matriz)):

        print(f'[ {matriz[x][y]} ]',end='')

        if matriz[x][y]%2 == 0 :
            soma += matriz[x][y]
            
    print('')

for x in range(0,len(matriz)):
    soma_segunda_coluna+= matriz[x][2]

for x in range(0,len(matriz)):
    if matriz[1][0]:
        maior_valor= matriz[1][0]
    if matriz[1][x] > maior_valor:
        maior_valor = matriz[1][x]

print(f'a soma dos pares é {soma}')
print(f'a soma da terceira coluna é {soma_segunda_coluna}')
print(f'o maior valor da segunda linha é {maior_valor}')

