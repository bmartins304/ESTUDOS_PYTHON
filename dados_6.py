import random
from time import sleep
from operator import itemgetter
jogos = {'jogador1': random.randint(1,6),
         'jogador2': random.randint(1,6),
         'jogador3': random.randint(1,6),
         'jogador4': random.randint(1,6)}
ranking = list()
for y,x in jogos.items():
    print(f'o {y} tirou {x} no dado')
    sleep(1)
ranking = sorted(jogos.items(),key=itemgetter(1),reverse=True)
for i,v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]} ')
    sleep(1)
        
