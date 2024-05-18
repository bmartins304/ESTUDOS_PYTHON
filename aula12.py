nome = str(input('qual o seu nome?'))

if nome == 'bruno':
    print('que nome bonito')
elif nome == 'ana' or nome == 'pedro' or nome == 'joao' :
    print('o seu nome é bem legal')
else:
    print('o seu nome é bem normal')
    
print('seja bem vindo, {}'.format(nome))