from time import sleep
mais_18 = 0
quantidade_homens = 0
quantidade_mulher_menos_20 = 0
res = ''
while True:
    res = ''
    genero = ''
    idade = int(input('informe sua idade: '))

    if idade > 18:
        mais_18 += 1

    while genero != 'M' and genero != 'F':
        genero = str(input('qual genero você se identifica?\nHOMEM[M] OU MULHER[F]: ')).upper()
        if genero != 'M' and genero != 'F':
            print('='*40)
            print('\033[35minforme um dado valido!\033[m')
            print('-'*40)
        if genero == 'M':
            quantidade_homens += 1
        
    if genero == 'F' and idade < 20:
        quantidade_mulher_menos_20 += 1


    print('-='*40)
    while res != 'N' and res != 'S':
        res = str(input('você quer continuar o cadastro? [S/[N]: ')).upper()

    if res == 'N':
        break
print('='*40)
print('ANALISANDO...')
sleep(2)
print('-'*40)
print(f'foram registradas {mais_18} pessoas acima de 18 anos.')
sleep(1)
print(f'foram cadastrados {quantidade_homens} homens.')
sleep(1)
print(f'foram cadastrados {quantidade_mulher_menos_20} mulheres com menos de 20 anos.')