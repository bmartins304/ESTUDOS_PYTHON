while True:
    num = int(input('digite o número da tabuada que você quer ver.\n(digite um número negativo para para o programa.): '))
    if num < 0:
        break
    for c in range(1 , 11):
        multiplicacao = num * c
        print(f'{num} X {c} = {multiplicacao}')    
print('programa encerrado!!!')
