pares = list()
impares = list()
dado = list()
for p in  range(0,7):
    n = int(input('digite um número: '))
    if n%2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    
dado.append(pares)
dado.append(impares)

for p in range(0,len(dado)):
    if p == 0:
        print(f'os valores pares são {dado[0]}')
    else:
        print(f'os valores impares são {dado[1]}')