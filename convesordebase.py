
num = int(input('digite um numero inteiro para ser convertido: '))
base = int(input('escolha a base de numero para a conversão:\n [1]binário\n [2]octal\n [3]hexadecimal\n informe o número da opção: '))

if base == 1:
    conversao = bin(num)
    print('o numero \033[33m{}\033[m convertido em binario é: \033[34m{}\033[m'.format(num,conversao[2:]))
elif base == 2:
    conversao = oct(num)
    print('o numero \033[31m{}\033[m convertido em octal é: \033[32m{}\033[m'.format(num,conversao[2:]))
elif base == 3:
    conversao = hex(num)
    print('o numero \033[35m{}\033[m convertido em hexadecimal é: \033[36m{}\033[m '.format(num,conversao[2:]))
else:
    print('informe uma opção valida!!')
   