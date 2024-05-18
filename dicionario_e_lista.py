cadastro = dict()
pessoas = list()
mulheres = list()
idade_acima_media = list()
tot= total_idade = media = 0
while True:
    cadastro['nome'] = str(input('Nome: ')).upper()
    while True:
        cadastro['genero'] = str(input(f'Qual o genero do(a) {cadastro["nome"]} [M]/[F] : ')).upper()
        if cadastro['genero'] == 'M' or 'S':
            break
        else:
            print('opção invalida')
    cadastro['idade'] = int(input(f'Qual é a idade do(a) {cadastro["nome"]}: '))
    if cadastro['genero'] == 'F':
        mulheres.append(cadastro.copy())
    pessoas.append(cadastro.copy())
    tot+=1
    total_idade += cadastro['idade']    
    media = total_idade/tot
    resp = str(input('Quer continuar?[S]/[N]')).upper()
    if resp == 'N':
        break
for x in pessoas:
    if x['idade'] > media:
        idade_acima_media.append(x)
print('-='*40)
print(f'o total cadastro foi de {tot} pessoas')
print(f'a media das idade é {media:.2f}')
print(f'lista somente com mulheres {mulheres}')
print(f'pessoas com a idade acima da média {idade_acima_media}')
