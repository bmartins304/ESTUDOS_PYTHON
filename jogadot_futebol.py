aproveitamento = dict()
gols = list()
total = 0
aproveitamento['nome'] = str(input('Nome: ')).upper()
jogos = int(input('Quantidade de jogos: '))
for y in range(0,jogos):
    quantidade_gols= int(input(f'quantidade de gols no jogo {y}: '))
    total += quantidade_gols
    gols.append(quantidade_gols)
aproveitamento['jogos'] = gols 
aproveitamento['total'] = total
print('-='*40)
print(aproveitamento)
print('-='*40)
for k,v in aproveitamento.items():
    print(f'{k} tem o valor {v}')
print('-='*40)
print(f'o jogador {aproveitamento["nome"]} jogou {jogos} partidas')
for p, k in enumerate(gols):
    print(f'na partida {p} fez {k}')
print(f'fez um total de {total} gols')
    