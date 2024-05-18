from datetime import date

ano_nascimento = int(input('informe o ano de nascimento do atleta: '))

ano_atual = date.today().year
idade_atleta = ano_atual - ano_nascimento

if 7 >= idade_atleta <= 9:
    print('categoria do atleta: MIRIM')
elif  idade_atleta <= 14:
    print('categoria do atleta: INFANTIL')
elif idade_atleta <= 19:
    print('categoria do atleta: JÚNIOR')
elif  idade_atleta <= 25:
    print('categoria do atleta: SÊNIOR')
else:
    print('categoria do atleta: MASTER')