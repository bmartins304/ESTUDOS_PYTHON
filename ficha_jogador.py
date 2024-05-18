

def ficha(nome='<desconhecido>',gol=0):
     print(f'o jogador {nome} fez {gol} gols')
        

nome = str(input('Qual o nome do jogador: '))
gols = str(input('Quantidade de gols: '))
if nome == '' and gols == '':
     ficha()
else:
     ficha(nome,gols)
      

