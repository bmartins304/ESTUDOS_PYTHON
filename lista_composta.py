dados = list()                                  
informacoes = list()
total_cadastro = mais_pesado = menos_pesado = 0

while True:
    informacoes.append(str(input('insira o nome: ')))
    informacoes.append(float(input('qual o peso: ')))
    dados.append(informacoes[:])
    informacoes.clear()
    total_cadastro += 1
    resp = str(input('deseja continuar cadastrando? [S]/[N]')).upper()
    if resp == 'N':
        break

for p,n in enumerate(dados):
    if p == 0:
        mais_pesado = n[1]
        menos_pesado = n[1]
    if n[1] >= mais_pesado:
        mais_pesado = n[1]       
    if n[1] <= menos_pesado:
        menos_pesado = n[1]
print('-'*50)   
print(f'foram cadastradas {total_cadastro} pessoas')

print(f'o maior peso foi de {mais_pesado} das pessoas: ',end=' ')       
for p in dados:
    if p[1] == mais_pesado:
        print(f'{p[0]}',end=', ')
print('')

print(f'o menor peso foi de {menos_pesado} das pessaos: ',end=' ')
for p in dados:
    if p[1] == menos_pesado:
        print(f'{p[0]}',end=', ')

    
    


