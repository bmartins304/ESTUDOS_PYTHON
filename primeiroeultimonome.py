nome = str(input('digite o seu nome completo: ')).strip()
pri = nome.split()
ult = pri[len(pri)-1]
print('o seu nome completo é: {}'.format(nome))
print('o seu primerio nome é: {}'.format(pri[0]))
print('o seu ultimo nome é: {}'.format(ult))