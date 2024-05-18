aproveitamento = dict()
aproveitamento_total = list()
gols = list()
total = 0

while True:
    total = 0
    aproveitamento.clear()
    aproveitamento['nome'] = str(input('Nome: ')).upper()
    jogos = int(input('Quantidade de jogos: '))
    gols.clear()
    for y in range(0,jogos):
        quantidade_gols= int(input(f'quantidade de gols no jogo {y}: '))
        total += quantidade_gols
        gols.append(quantidade_gols)
        
    aproveitamento['jogos'] = gols[:]
    aproveitamento['total'] = total
    aproveitamento_total.append(aproveitamento.copy())
    resp = str(input('Quer continuar cadastradando?[S]/[N]')).upper()
    if resp == 'N':
        break


print('-='*40)
print(f'{'ID':<4}{'NOME':<15}{'GOLS':>4}{'TOTAL':>15}')
for k,v in enumerate(aproveitamento_total):
    print(f'{k:<4}',end="")
    for d in v.values():
        print(f'{str(d):<15}',end="")
    print()
print('-='*40)

while True:
    busca = int(input('Mostrar dado de qual jogador:[999 para programa]'))  

    if busca == 999:
        print('programa encerrado!')
        break
    if busca <= len(aproveitamento_total) - 1:
        print(f'-LEVANTAMENTO DO JOGADOR {aproveitamento_total[busca]["nome"]}')
        for k,x in enumerate(aproveitamento_total[busca]['jogos']):
            print(f'na {k} partida fez {x} gols')
            
    else:
        print(f'ERRO!jogador não encontrado com o código {busca}.')
    print('-='*40)
'''print('-='*40)
print(f'o jogador {aproveitamento["nome"]} jogou {jogos} partidas')
for p, k in enumerate(gols):
    print(f'na partida {p} fez {k}')
print(f'fez um total de {total} gols')'''
    