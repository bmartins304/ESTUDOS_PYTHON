from datetime import date
ano_atual = date.today().year

def voto(ano_nascimento):
    
    idade_atual = ano_atual - ano_nascimento
    if idade_atual <16:
        letras = 'NAO VOTA!'
    elif idade_atual >= 16 and idade_atual <18:
        letras = 'VOTO OPCIONAL!'
    elif idade_atual < 66:
        letras = 'VOTO OBRIGATORIO!'
    else:
        letras = 'VOTO OPCIONAL!'
    return str(letras)

#programa principal
entrada = int(input('Qual o ano de nascimento: '))
idade = ano_atual - entrada
print(f'com {idade} anos: {voto(entrada)} ')