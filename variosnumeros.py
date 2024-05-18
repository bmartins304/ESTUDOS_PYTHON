num = 0
soma = 0
quantidade = 0
while num != 999:
    num = int(input('digite um número:'))
    if num != 999:       
        quantidade+=1
        soma += num
print('a quantidade digitada foi {} e a soma dos números digitados foi de {}'.format(quantidade,soma))