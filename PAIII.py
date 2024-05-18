primeiro_termo = int(input('informe o primeiro termo da PA: '))
razao = int(input('informe a razão da PA: '))
variavel_nova = 0
t = 1
termo = 10
while termo != 0 :
    termo = int(input('você quer mostrar mais quantos termos dessa PA: '))
    variavel_nova += termo
    while t < variavel_nova + 1:
            pa = primeiro_termo+(t - 1)*razao
            print('{}o termo: {}'.format(t,pa))
            t+=1
print('programa encerrado!')           
