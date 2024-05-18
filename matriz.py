matriz = list()
vetor = list()
for x in range(0,3):
    for y in range(0,3):
        vetor.append(int(input(f'insira um valor para {x,y}: ')))
    matriz.append(vetor[:])
    vetor.clear()
print('¨'*40)
for x in range(0,len(matriz)):
    for y in range(0,len(matriz)):
        print(f'[ {matriz[x][y]} ]',end='')
    print('')
        