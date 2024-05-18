#desafio 1
num = int(input('digite um numero: '))
num2 = int(input('digite o segundo numero: '))
s = num + num2 
cores = {'limpa':'\033[m', 
         'amarelo':'\033[33m', 
         'verde':'\033[32m'}
print('a soma entre {}{}{} e {}{}{} vale {}'.format(cores['amarelo'],num,cores['limpa'], cores['verde'],num2,cores['limpa'] ,s))

