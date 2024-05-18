import random
from time import sleep
jokenpo = ['PEDRA','PAPEL','TESOURA']
pc = random.randint(0,2)
print('{:=^50}'.format(' SUPER JOKENPO '))
escolha = int(input('jogador 1 escolha:\n'
                    '[1] PEDRA\n'
                    '[2] PAPEL\n'
                    '[3] TESOURA\n-> '))

player = escolha - 1
print('JO...')
sleep(1.5)
print('JOKEN...')
sleep(1.5)
print('JOKENPO!!!')
sleep(1)
print('='*50)
print('jogador 1 = {} X jogador 2 = {}'.format(jokenpo[player],jokenpo[pc]))

if  player == pc:
    print('EMPATE!')
elif player == 0 and pc == 1:
    print('jogador 2 VENCEU!!')
elif player == 0 and pc == 2:
    print('jogador 1 VENCEU!!')
elif player == 1 and pc == 0:
    print('jogador 1 VENCEU!!')
elif player == 1 and pc == 2:
    print('jogador 2 VENCEU!!')
elif player == 2 and pc == 0:
    print('jogador 2 VENCEU!!')   
elif player == 2 and pc == 1:
    print('jogador 1 VENCEU!!')
else:
    print('jogada invalida!!')
