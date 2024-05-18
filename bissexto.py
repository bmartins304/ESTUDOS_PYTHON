from datetime import date

ano = int(input('digite o ano aqui ou digite 0 para pegar o ano atual: '))
ano0 = ano // 1 % 10
ano00 = ano // 10 % 10
if ano == 0:
    ano = date.today().year
    ano0 = ano // 1 % 10
    ano00 = ano // 10 % 10
if (ano0 == 0 and ano00 == 0):
    if( ano%400 == 0):                                   # if ano%4==0 and ano%100!=0 or ano%400 ==0:
        print('ano {} é bissexto!'.format(ano))
    else:
        print('esse ano {} nao é bissexto!'.format(ano))
elif(ano%4 == 0):
    print('ano {} é bissexto!'.format(ano))
else:
    print('esse ano {} nao é bissexto!'.format(ano))