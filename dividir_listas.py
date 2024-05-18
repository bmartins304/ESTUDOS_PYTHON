numeros = list()
numeros_pares = list()
nuemros_impares = list()
while True:
    num = int(input('digite um valor: '))
    numeros.append(num)
    if num % 2 == 0:
        numeros_pares.append(num)
    else:
        nuemros_impares.append(num)
    resp = str(input('deseja continuar digitando? [S]/[N]')).upper()
    if resp == 'N':
        break
print(f'a lista de numeros é {numeros}\n os números pares foram {numeros_pares}\ne os números ímpares foram {nuemros_impares}')