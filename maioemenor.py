n1 = int(input('digite o primeiro numero: '))
n2 = int(input('digite o segundo numero: '))
n3 = int(input('digite o terceiro numero: '))

if (n1 < n2) and (n1 < n3) :
    print('o menor numero é: {}'.format(n1), end=' & ')
elif(n2 < n1) and (n2 < n3):
    print('o menor numero é: {}'.format(n2),end=' & ')
else:
    print('o menor numero é: {}'.format(n3),end=' & ')


if (n1 > n2) and (n1 > n3):
    print('o mairo numero é: {}'.format(n1))
elif(n2 > n1) and (n2 > n3):
    print('o maior numero é: {}'.format(n2))
else:
    print('o maior numero é: {}'.format(n3))
    
        