lado_1 = float(input('informe o tamanho do primeiro lado do triangulo: '))
lado_2 = float(input('informe o tamanho do segundo lado do triangulo: '))
lado_3 = float(input('informe o tamanho do terceiro lado do triangulo: '))

soma_lado_1 = lado_1 + lado_2
soma_lado_2 = lado_2 + lado_3
soma_lado_3 = lado_1 + lado_2

if (soma_lado_1 > lado_3) and (soma_lado_2 > lado_1) and (soma_lado_3 > lado_2):
    print('-'*50)
    print('esses lados {}/{}/{} podem formar um triangulo!'.format(lado_1,lado_2,lado_3))

    if (lado_1 == lado_2) and (lado_2 == lado_3):
        print('o triangulo formado será um EQUILÁTERO, pois todos os seus lados são iguais.')
    elif (lado_1 == lado_2) or (lado_2 == lado_3) or (lado_1 == lado_3):
        print('o triangulo formado será um ISÓSCELES, pois seus dois lados são  iguais.')
    else:
        print('o triangulo formado será um ESCALENO, pois seus lados são diferentes.')
        
else:
    print('-'*50)
    print('esses lados {}/{}/{} não podem formar um triangulo!'.format(lado_1,lado_2,lado_3))
