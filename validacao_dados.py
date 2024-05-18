def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO! Digite um número inteiro valido.')
        if ok:
            break
    return valor

n=leiaint('digite um numero: ')
print(f'o valor digitado foi {n}')
