n1 = int(input('informe um número para a comparação:  '))
n2 = int(input('informe o segundo número para a comparação: '))

if n1>n2:
    print('o primeiro número é o maior: \033[33;42m{}\033[m'.format(n1),end=" > ")
    print('o segundo número é o menor: \033[33;42m{}\033[m'.format(n2))
elif n2>n1:
    print('o segundo número é o maior: \033[33;42m{}\033[m'.format(n2),end=" > ")
    print('o primeiro número é o menor: \033[33;42m{}\033[m'.format(n1)) 
else:
    print('ambos os números são iguais.')