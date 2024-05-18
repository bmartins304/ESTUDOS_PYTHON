sair = 0
while sair != 5:
    res = 0
    n1 = float(input('primeiro número: '))
    n2 = float(input('segundo número: '))
    while res != 4:
        print('='*50)
        res = int(input('menu de opções:\n[1] somar\n[2] multiplicas\n[3] maior\n[4] novos números\n[5] sair do programa\nescolha a opção: '))
        if res == 1:
            soma = n1 + n2
            print('a soma dos números {} e {} tem como resultado {}'.format(n1,n2,soma)) 
        elif res == 2:
            multiplicar =  n1 * n2
            print('a multiplicação dos números {} e {} tem como resultado {}'.format(n1,n2,multiplicar))
        elif res == 3:
            if n1 > n2:
                print('o maior número é o {}'.format(n1))
            else:
                print('o maior número é o {}'.format(n2))
        elif res == 5:
            res = 4
            sair = 5
print('programa finalizado')