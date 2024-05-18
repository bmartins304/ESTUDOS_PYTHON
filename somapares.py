quant = 0
par = 0
for i in range(1,7):
    num = int(input('informe o {}o número: '.format(i)))
    if num % 2 == 0:   
        par = par + num
        quant += 1
print('a soma dos numeros é : {}'.format(par) )   
print('a quantidade de numeros somoados foram: {}'.format(quant))   
