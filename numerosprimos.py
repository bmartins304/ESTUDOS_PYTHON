valor = 0
num = int(input('informe um numero para verificar se é PRIMO: '))
print('divisivel por :',end=" ")
for c in range(1,num + 1):
    if num%c == 0:
        valor += 1
        print(c,end=',')
if valor != 2 :
    print('\nesse numero {} não é primo!'.format(num))
else:
    print('\nesse numero {} é PRIMO!'.format(num))