r = True
while r == True:
    genero = str(input('Qual o seu gênero: [M]/[F] ')).upper()
    
    if genero == 'M' or genero == 'F':
        print('dado valido')
        r = False
    else:
        print('genero invalido!!!')
    