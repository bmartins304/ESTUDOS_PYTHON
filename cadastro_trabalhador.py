from datetime import date
cadastro = dict()
cadastro['nome'] = str(input('Nome: ')).upper()
ano_nascimento = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
cadastro['idade'] = idade
cadastro['carteira'] = int(input('Carteira de Trabalho(0: NÃO TEM): '))

if cadastro['carteira'] != 0:
    cadastro['contratacao'] = int(input('Ano de contratação: '))
    cadastro['salario'] = float(input('valor do salario recebido: '))
    idade_aposentadoria = (cadastro['contratacao'] + 35) - ano_nascimento
    cadastro['aposentadoria'] = idade_aposentadoria
    print('-='*40)
    for k,v in cadastro.items():
        print(f'{k} tem o valor {v}')
else:
    print('cadastro realizado!')