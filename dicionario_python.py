cadastro= dict()
cadastro['nome'] = str(input('NOME: ')).upper()
cadastro['media'] = float(input(f'Qual a média do {cadastro["nome"]}: '))
if cadastro['media'] >= 7.0:
    cadastro['situacao'] = 'Aprovado'
else:
    cadastro['situacao'] = 'Reprovado'
for k , x in cadastro.items():
    print(f'{k} é igual a {x}')