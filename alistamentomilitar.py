from datetime import date

ano_nascimento = int(input('informe o ano do seu nascimento: '))
ano_atual = date.today().year
idade_usuario = ano_atual - ano_nascimento

#print('a sua idade atual é: {}'.format(idade_usuario))

if idade_usuario < 18:
    falta_alistamento =  18 - idade_usuario 
    ano_faltante = falta_alistamento + ano_atual
    print('você ira realizar o alistamento em {} ano(s)\ndeverá procurar uma junta militar em {} anos'.format(falta_alistamento,ano_faltante))
elif idade_usuario == 18:
    print('Esse será o ano que você completará 18 anos.\nProcure o serviço de alistamento mais proximo da sua cidade.')
else:
    passou_alistamento = idade_usuario - 18
    ano_faltante = ano_atual - passou_alistamento
    print('o seu tempo de se alistar passou {} ano(s)\n ano do alistamento: {}'.format(passou_alistamento, ano_faltante))