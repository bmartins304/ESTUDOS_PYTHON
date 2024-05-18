def contador(*num):
    for valor in num:
        print(f' {valor}',end='')
    print()
    tam = len(num)
    print(f'a quantidade de item é {tam}')
contador(8,4,3)
contador(1,2)